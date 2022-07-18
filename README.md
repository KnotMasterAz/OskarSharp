
<p align="center">
<img src="OskarSharp.png" alt="OskarSharp logo circle logo" style="height: 300px;"/><br>
<h1 align="center">OskarSharp</h1>
</p>

A simple, statically typed programming language focused on code generation powered by the dotnet framework

# CURRENTLY BROKEN, REWRITE UNDERWAY!

## Components
### Languages
- [OskarSharp](specification/oskarsharp.md) (programming language, transpiled, .oskar)
- [OskarSharper](specification/oskarsharper.md) (preprocessor language, interpreted, N/A)
- [OskarSharpKnot](specification/oskarsharpknot.md) (generated tokens, generated, .knot)
## Parts
- Az (transpiler for interpreting a single OskarSharp file or project.oskar file, into a OskarSharp Token Language and then transpile that into C#)
- OskarSharp (OskarSharp & OskarSharp Embed Language)


### Important
**NOTE**: A major rewrite is in progress, the old transpiler is being replaced and language spec being updated!

### Goals
- Configure the project using the language
- Advance code generation
- Imperative and strongly typed
- Cross platform
- Simple
- Enjoyable

## To-do
- [WIP] Finalise new spec for OskarSharp
- [ ] Finalise new spec for OskarSharper
- [WIP] Finalise new spec for OskarSharpKnot
- [WIP] Write a tokeniser
- [ ] Implement new transpiler
- [ ] Remove legacy from project

### Licence
[Licence](LICENSE)
