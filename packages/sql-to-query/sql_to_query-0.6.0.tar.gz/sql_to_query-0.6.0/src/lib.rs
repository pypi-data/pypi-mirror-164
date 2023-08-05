#![recursion_limit = "1024"]

#[macro_use]
extern crate pest_derive;

use pest::prec_climber::{Assoc, Operator, PrecClimber};
use serde_json::json;

//use pest::error::Error;
use pest::Parser;
use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

#[pyfunction]
fn get_query(where_query: String) -> PyResult<String> {
    let result = convert(where_query, 0, 100, vec![], vec![]);

    match result {
        Ok(value) => Ok(value.to_string()),
        Err(error) => {
            println!("{:?}", error);
            Err(PyRuntimeError::new_err(error.expected))
        }
    }
}

#[pymodule]
fn sql_to_query(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_query, m)?)?;
    Ok(())
}

#[derive(Parser)]
#[grammar = "expr.pest"]
struct ExprParser;

/// error occurred when parsing user input
#[derive(Debug)]
pub struct ParseError {
    pub location: pest::error::InputLocation,
    pub expected: String,
}

/// convert user input to Elasticsearch DSL
/// example :
/// ```
/// extern crate elastic_query;
/// use elastic_query::convert;
/// convert("a = 1 and b = 2 and c = 3".to_string(), 0, 1000, vec![], vec![]);
/// ```
/// will generate result :
/// ```json
/// {
///	"query": {
///		"bool": {
///			"filters": [{
///				"bool": {
///					"filters": [{
///						"term": {
///							"a": {
///								"value": "1"
///							}
///						}
///					}, {
///						"term": {
///							"b": {
///								"value": "2"
///							}
///						}
///					}]
///				}
///			}, {
///				"term": {
///					"c": {
///						"value": "3"
///					}
///				}
///			}]
///		}
///	}
///}
/// ```
pub fn convert(
    query: String,
    from: i32,
    size: i32,
    sort: Vec<&str>,
    aggs: Vec<&str>,
) -> Result<serde_json::Value, ParseError> {
    let parse_result = ExprParser::parse(Rule::expr, query.as_str());
    match parse_result {
        Ok(mut expr_ast) => {
            let ast = generate_ast(expr_ast.next().unwrap());
            let dsl = walk_tree(ast, true);

            let mut result = json!({
               "query": dsl,
               "from" : from,
               "size" : size,
            });

            if sort.len() > 0 {
                result["sort"] = build_sort(sort);
            }

            if aggs.len() > 0 {
                result["aggregations"] = build_aggs(aggs);
            }

            return Ok(result);
        }
        Err(err) => {
            // TODO: more friendly error
            Err(ParseError {
                location: err.location,
                expected: "".to_string(),
            })
        }
    }
}

fn build_aggs(aggs: Vec<&str>) -> serde_json::Value {
    let mut result: serde_json::Value = json!({});
    aggs.iter().enumerate().rev().for_each(|(idx, &field)| {
        let previous_result = result.clone();

        let size = if idx == 0 { 200 } else { 0 };

        result = json!({
            field : {
                "terms" : {
                    "field" : field,
                    "size" : size,
                }
            }
        });

        if previous_result.as_object().unwrap().len() > 0 {
            result[field]["aggregations"] = previous_result;
        }
    });

    result
}

fn build_sort(sort: Vec<&str>) -> serde_json::Value {
    sort.iter()
        .map(|&s| {
            let mut elem: Vec<&str> = s.split_whitespace().collect();
            if elem.len() < 2 {
                elem.push("asc");
            }
            json!({elem[0] : elem[1]})
        })
        .collect()
}

use pest::iterators::Pair;

#[derive(Debug)]
enum Expression {
    CompExpr(String, Rule, String),
    AndExpr(Box<Expression>, Box<Expression>),
    OrExpr(Box<Expression>, Box<Expression>),
}

fn generate_ast(pair: Pair<Rule>) -> Expression {
    let climber = PrecClimber::new(vec![
        Operator::new(Rule::and_op, Assoc::Left) | Operator::new(Rule::or_op, Assoc::Left),
    ]);

    consume(pair, &climber)
}

fn consume(pair: Pair<Rule>, climber: &PrecClimber<Rule>) -> Expression {
    let atom = |pair| consume(pair, climber);
    let infix = |lhs, op: Pair<Rule>, rhs| match op.as_rule() {
        Rule::and_op => Expression::AndExpr(Box::new(lhs), Box::new(rhs)),
        Rule::or_op => Expression::OrExpr(Box::new(lhs), Box::new(rhs)),
        _ => unreachable!(),
    };

    match pair.as_rule() {
        Rule::expr => {
            let pairs = pair.into_inner();
            climber.climb(pairs, atom, infix)
        }
        Rule::paren_bool => pair.into_inner().next().map(atom).unwrap(),
        Rule::comp_expr => {
            let mut iter = pair.into_inner();
            let (lhs, op, rhs) = (
                iter.next().unwrap().as_str().to_string(),
                iter.next().unwrap().into_inner().next().unwrap().as_rule(),
                iter.next().unwrap().as_str().to_string(),
            );
            return Expression::CompExpr(lhs, op, rhs);
        }
        _ => unreachable!(),
    }
}

fn walk_tree(expr: Expression, is_root: bool) -> serde_json::Value {
    match expr {
        Expression::AndExpr(lexpr, rexpr) => {
            let (left_val, right_val) = (walk_tree(*lexpr, false), walk_tree(*rexpr, false));
            return serde_json::json!({
                "bool" : {
                    "filters" : [left_val, right_val]
                }
            });
        }
        Expression::OrExpr(lexpr, rexpr) => {
            let (left_val, right_val) = (walk_tree(*lexpr, false), walk_tree(*rexpr, false));
            return serde_json::json!({
                "bool" : {
                    "should" : [left_val, right_val]
                }
            });
        }
        Expression::CompExpr(lhs, operator, rhs) => {
            #[rustfmt::skip]
            let result = match operator {
                Rule::eq | Rule::like => json!({"term" : {lhs : {"value" : rhs}}}),
                Rule::gte => json!({"range" : {lhs : {"from" : rhs}}}),
                Rule::lte => json!({"range" : {lhs : {"to" : rhs}}}),
                Rule::gt => json!({"range" : {lhs : {"gt" : rhs}}}),
                Rule::lt => json!({"range" : {lhs : {"lt" : rhs}}}),
                Rule::neq => json!({"bool" : {"must_not" : [{"term" : {lhs : {"value" : rhs}}}]}}),
                Rule::op_in => {
                    let rhs = rhs.replace("\'", "\"");
                    let r_vec: Vec<&str> = rhs
                        .trim_start_matches("(")
                        .trim_end_matches(")")
                        .split(",")
                        .map(|v| v.trim())
                        .collect();
                    json!({"terms" : {lhs : r_vec}})
                }
                Rule::op_not_in => {
                    let rhs = rhs.replace("\'", "\"");
                    let r_vec: Vec<&str> = rhs
                        .trim_start_matches("(")
                        .trim_end_matches(")")
                        .split(",")
                        .map(|v| v.trim())
                        .collect();
                    json!({"bool" : {"must_not" : {"terms" : { lhs : r_vec}}}})
                }

                _ => unreachable!(),
            };

            if is_root {
                return json!({"bool" : {"filters" :[result]}});
            }
            return result;
        }
    }
}

#[cfg(test)]
mod tests {
    use serde_json::json;

    #[allow(dead_code)]
    struct TestCase<'a> {
        input: (&'a str, i32, i32, Vec<&'a str>, Vec<&'a str>), // query, from, size, sort, agg
        output: serde_json::Value,
        comment: &'a str,
    }

    #[test]
    fn test_convert() {
        let test_cases: Vec<TestCase> = vec![
            TestCase {
                input: ("a=1", 1000, 1000, vec![], vec![]),
                output: json!({"query" : {"bool" : {"filters" : [{"term" :{"a" : {"value" : "1"}}}]}}, "from" : 1000, "size" : 1000}),
                comment: "equal expression test",
            },
            // TestCase {
            //     input: ("a='asd'", 1000, 1000, vec![], vec![]),
            //     output: json!({"query" : {"bool" : {"filters" : [{"term" :{"a" : {"value" : "asd"}}}]}}, "from" : 1000, "size" : 1000}),
            //     comment: "equal expression test",
            // },
            // TestCase {
            //     input: ("a=a", 1000, 1000, vec![], vec![]),
            //     output: json!({"from":1000,"query":{"bool":{"filters":[{"term":{"a":{"value":"1"}}}]}},"size":1000,"sort":[{"a":"asc"},{"b":"desc"}]}),
            //     comment: "sort test",
            // },
            TestCase {
                input: ("a=1", 0, 1000, vec!["a asc", "b"], vec![]),
                output: json!({"from":0,"query":{"bool":{"filters":[{"term":{"a":{"value":"1"}}}]}},"size":1000,"sort":[{"a":"asc"},{"b":"asc"}]}),
                comment: "sort test",
            },
            TestCase {
                input: ("a in (1,2,3)", 1000, 1000, vec![], vec![]),
                output: json!({"from":1000,"query":{"bool":{"filters":[{"terms":{"a":["1","2","3"]}}]}},"size":1000}),
                comment: "in expression test",
            },
            TestCase {
                input: ("a in (   1, 2,  3)", 1000, 1000, vec![], vec![]),
                output: json!({"from":1000,"query":{"bool":{"filters":[{"terms":{"a":["1","2","3"]}}]}},"size":1000}),
                comment: "auto trim space test",
            },
            TestCase {
                input: ("a in (   1, 2,  3)", 1000, 1000, vec![], vec!["a", "b"]),
                output: json!({"aggregations":{"a":{"aggregations":{"b":{"terms":{"field":"b","size":0}}},"terms":{"field":"a","size":200}}},"from":1000,"query":{"bool":{"filters":[{"terms":{"a":["1","2","3"]}}]}},"size":1000}),
                comment: "aggregation test",
            },
            TestCase {
                input: ("a = 1 and (b = 2 and (c = 3))", 0, 1000, vec![], vec![]),
                output: json!({"from":0,"query":{"bool":{"filters":[{"term":{"a":{"value":"1"}}},{"bool":{"filters":[{"term":{"b":{"value":"2"}}},{"term":{"c":{"value":"3"}}}]}}]}},"size":1000}),
                comment: "paren expr test",
            },
            TestCase {
                input: ("a = 1 and b = 2 and c = 3", 0, 1000, vec![], vec![]),
                output: json!({"from":0,"query":{"bool":{"filters":[{"bool":{"filters":[{"term":{"a":{"value":"1"}}},{"term":{"b":{"value":"2"}}}]}},{"term":{"c":{"value":"3"}}}]}},"size":1000}),
                comment: "left association test",
            },
            TestCase {
                input: (
                    "a = 1 and b = 2 and c = 3 and d = 4",
                    0,
                    1000,
                    vec![],
                    vec![],
                ),
                output: json!({"from":0,"query":{"bool":{"filters":[{"bool":{"filters":[{"bool":{"filters":[{"term":{"a":{"value":"1"}}},{"term":{"b":{"value":"2"}}}]}},{"term":{"c":{"value":"3"}}}]}},{"term":{"d":{"value":"4"}}}]}},"size":1000}),
                comment: "left association test",
            },
            TestCase {
                input: ("a = 1 or b = 2", 0, 1000, vec![], vec![]),
                output: json!({
                    "from":0,
                    "query":{
                        "bool":{
                            "should":[
                                {
                                    "term":{"a": {"value": "1"}}
                                },
                                {
                                    "term":{"b": {"value": "2"}}
                                },
                            ],
                        }
                    },
                    "size":1000
                }),
                comment: "or",
            },
        ];
        test_cases.iter().for_each(|case| {
            let output = super::convert(
                case.input.0.to_string(),
                case.input.1,
                case.input.2,
                case.input.3.clone(),
                case.input.4.clone(),
            )
            .unwrap();
            // println!("{}", output);
            assert_eq!(output, case.output)
        });
    }
}
