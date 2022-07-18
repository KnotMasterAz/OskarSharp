# Oskar Sharp Knot Proposal Specification

This is the specification for OskarSharpKnot (token language), for specification details on the language, see [OskarSharp](oskarsharp.md)

## Token schema
Tokens are composed of a opening tag `<tag>` and closing tag `</tag>` and the value of the token inside that tag, the tag name should correspond to the category the token is a part of.
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