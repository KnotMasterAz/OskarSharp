# OskarSharp

<p align="center">
<img src="OskarSharp.png" alt="OskarSharp logo circle logo" style="height: 500px;"/><br>
A simple, statically typed programming language focused on code generation, compiling into C#
</p>


### Important
**NOTE**: A major rewrite is in progess, the old transpiler is being replaced and language spec being updated!

**NOTE**: This is not a compiler and merely "finds and replaces" the instances of text to their C# counterpart as such will replace this text inside of comments and strings so should **not** be used in production!

### Licence
[Licence](LICENSE)


### Goals
- Advance code generation
- Imperative and strongly typed
- Cross platform
- Simple
- Enjoyable

## To-do
- [ ] Change file extension to .oskar in code directory
- [x] Console template
- [X] Remove requirement on bash (rewrite build script in Python)
- [X] Version validation
- [X] Automatic ; insertion at the end of lines
- [X] Add logging
- [ ] Interactive mode (type so many commands and let them be run after a special compile/execute command is run)
- [ ] Replace fun:<datatype> syntax for something more simple
- [ ] Replace C# . to access properties with an _ for non-structs
- [ ] Multi file support
- [ ] More functions
- [ ] Generate single code file (not a main file)
- [ ] Structs (custom data type) support
- [ ] Implement generics
- [ ] Arrays
- [ ] Lists
- [ ] Preprocessor support (do not rely on the C# Preprocessor, that should be used using csh.#DIRECTIVE)
- [ ] Unity support
- [ ] Parse code instead of find and replace
- [ ] Write the transpiler and build in KnotsSharp
- [ ] Write documentation for the language
- [ ] language spec
- [ ] Language tests
- [ ] Support for OOP features where needed to work with existing code

## Dependencies
- Python 3
- Dotnet

## Build
```sh
    git clone https://github.com/KnotMasterAz/OskarSharp.git
    cd OskarSharp
    python legacy/start.py code/hello.oskar --run --Console # Compile using the legacy compiler
```

## Examples

### Hello, World!
```cs
//V0.1.0+
fun:pure main() {
    print("Hello, Knots!")
}
```

### Calculator
```cs
//V0.1.1+
fun:pure main() {
    print_online("Number 1: ")
    float64 num1 = csh.Convert.ToDouble(read())

    print_online("Operator (+, -, *, /): ")
    string op = read()

    print_online("Number 2: ")
    float64 num2 = csh.Convert.ToDouble(read())

    float64 result = sum(num1, op, num2)

    print($"{num1} {op} {num2} = {result}")

    print("Hit enter to close program!")
    read()
}

fun:float64 sum(float64 num1, string op, float64 num2) {   
    switch (op) {
        case "*":
            return num1 * num2

        case "/":
            return num1 / num2

        case "-":
            return num1 - num2

        case "+":
            return num1 + num2
        
        default:
            print("Error: Invalid operator!");
            return -404
    }
}
```
