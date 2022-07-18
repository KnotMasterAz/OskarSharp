# Oskar Sharp Knot Proposal Specification

This is the specification for OskarSharpKnot (token language), for specification details on the language, see [OskarSharp](oskarsharp.md)

## Token schema
Tokens are composed of a general tag (category) e.g. `Datatype`, a separator ` <;;> ` and the value of the tag (token itself) e.g. `i8`.

Below is an example of tokens generated from a a simple hello world program:
```yaml
Access <;;> pub
Datatype <;;> i64
Identifier <;;> main
Symbols <;;> ->
Datatype <;;> str
Separator <;;> [
Separator <;;> ]
Identifier <;;> args
Separator <;;> {
Identifier <;;> print
Separator <;;> (
Text <;;> Hello, knots!
Separator <;;> )
Comment <;;> 
Separator <;;> }

```

# Tag list
- Access
- Datatype
- Identifier
- Symbol
- Separator
- Text
- Comment
- Keyword
- Operator
- LogicalOperator
- ComparisonOperator