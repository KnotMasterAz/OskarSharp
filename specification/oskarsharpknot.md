# Oskar Sharp Knot Proposal Specification

This is the specification for OskarSharpKnot (token language), for specification details on the language, see [OskarSharp](oskarsharp.md)

## Token schema
Tokens are composed of a opening tag `<tag>` and closing tag `</tag>` and the value of the token inside that tag, the tag name should correspond to the category the token is a part of.
```html
<access>pub</access>
<static>mut</static>
<datatype>str</datatype>
<identifier>my_variable</identifier>
<operator>assignment</operator>
<string_literal>My super simple text token</string_literal>
```

# Tag list
- `<access>`
- `<static>`
- `<operator>`
- `<identifier>`
- `<logical_operators>`
- `<comparison_operator>`
- `<string_literal>`
- `<integer_literal>`
- `<separators>`
- `<keyword>`
- `<online_comment>`
- `<comment>`
- `<datatype>`