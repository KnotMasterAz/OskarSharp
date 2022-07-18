# Oskar Sharp Proposal Specification

This is the specification for OskarSharp, for specification details on the preprocessor, see [OskarSharper](oskarsharper.md)

## Datatypes

```lisp
i8 ; integer8
i16 ; integer16
i32 ; integer32
i64 ; integer64
u8 ; unsigned integer8
u16 ; unsigned integer16
u32 ; unsigned integer32
u64 ; unsigned integer64
f32 ; float32
f64 ; float64
bool ; boolean
str ; string
pure ; no-return type
```

## Access modifiers

```lisp
pub ; Variable is accessible anywhere in the program
priv ; Variable is only accessible in that file
restricted ; variable is accessible anywhere in that directory and sub-directories
```

## Variables
Variables take the default scope `pub` and are initialised with a default value, numbers are `0`, strings are `""` and booleans are `false`.

Constants must have their value provided when defined

`mut` will define a mutable variable and `const` will define a constant. The compiler will allow you to specify if variables without a `mut`/`const` should be interpreted as a constant or mutable. However, it is good practice to be explicit.

```lisp
; <Access modifier?> <mut/const?> <name> <assignment? (:=)> <value>
pub mut i8 my_byte := 10
```

## Procedures
Procedures are defined much like variables, using the following schema `<Access modifier>` (optional) `<return type>` `<name>` `->` `<arg type> <arg>` (separated by `,`). The keyword `ret <value>` will return that value, if `ret` is given no value, it will return that types default value.
For example, a simple function to add two `i8`'s together:

```lisp
priv i8 add -> i8 a, i8 b {
    ret a + b ; return a + b
}
```
Invocation of procedures is extremely easy, `<name>(args)` will invoke the procedure, a variable can be captured from the return via `<variable type>` `<variable name>` `:=` and then invoke the procedure.
For instance, using the previously defined `add` procedure:

```lisp
i8 sum := add(a, b)
```

## Events and signals
Events are like procedures except have no return value, no arguments and are scope-less. A signal can be fired by typing the keyword `fire` followed by `event_name` which will fire a signal. A signal is destroyed once an event uses that signal but it is kept around till the end of the program cycle so nay other events will be fired using the same signal.

To create an event, the keyword `event` `<event name>` will create an event.

**Note:** events are managed, if you fire an event, it will not be usable by events later in the source file until the next program cycle and events are not run in any specific order.

An example of an event and signal

```lisp 
event my_event {
    fire my_event ; will fire itself constantly
}

```

## Default aliases
By default, OskarSharp comes with aliases for common things such as a default int type and float type
- `float` is aliased to `f64`
- `int` is aliased to `i64`
- `uint` is aliased to `u64`
- `unless` is aliased to `if not`


# Loops and iteration
There are several different types of loops as standard in OskarSharp, `forever`, `while`, `for`, `loop` `each` loops.

The simplest loop is the `forever` loop.

```lisp
forever {
    ; this will constantly run
}
```

The `while` loop will continue to run as long as the expression evaluates to true.

```lisp
while i = 1 {
    ; run while i is 1
}
```

The simple `loop` will repeat that loop a set number of times.

```lisp
loop 10 {
    ; runs 10 times
}
```

The most powerful loop is the `for` loop, the first part defines a variable, second a condition to continue and finally what to do after each iteration

```lisp
for i8 i := 0, i < 10, i++ {
    ; this will create a variable i and set it to zero
    ; increasing it by one each iteration
    ; continuing as long as i is less than ten
}
```
The `each` loop, iterates through a data strcuture and allows the programmer to use that value

```lisp
each my_i8 in my_array_of_i8 {
    ; while loop through each value in my_array_of_i8
    ; my_i8 will store the value of that
}
```

# Comments
The language only supports one type of comment, anything after `;` till the end of line is not interpreted as code but as a comment.

Comments can go at the end of a line or at the start of the line.

# Escape and special characters
The escape character is `\` so if you wanted to nest a `"` inside a string, you would type `"My \"text\""` for example.

To start a new line, type, `\n` and `\t` for a tab. These can be escaped, e.g. `\\t` will show as `\t` in the program.

## Control flow

### Control keywords
The `top` keyword will return to the top of the procedure/loop/event, in the case of the loop, counting as an iteration.

The `quit` keyword will exit a loop and in a procedure, will be treated as `ret` with no other values provided. Events should use `quit` instead of `ret`.

### If statements
The most often used method of control flow is the `if` statement, formed by `if CONDITION`, additionally, if statements allow combining multiple checks, `elseif` (else if) (requires condition) and `finally` (non of the above conditions met) (cannot have a condition). `finally` must go after any if conditions and if else statements, if else must go before finally and after an if statement.

```lisp
if i = 10 {
    ; i is 10
} elseif i = 11 or i = 12 {
    ; i is either 11 and 12
} elseif i = 10 and not i = 10 {
    ; this condition is impossible
} finally {
    ; i is not 10, 11 or 12
}
```

### Case statements
A `case` statement allows you check a variable for multiple different values without needing to write a load of if statements.

You use `case` to check the variable, `when` to check for that value and `else` as a default in-case no other conditions were met, like `finally`

An example for checking the value of `my_var`:

```lisp
case my_var {
    when 1 {
        ; my_var is 1
    }
    when 2 {
        ; my_var is 2
    }
    when 3 {
        ; my_var is 3
    }
    when 4,5,6 {
        ; my_var is either 4, 5 or 6
    }
    else {
        ; my_var is not 1, 2, 3, 4, 5 or 6
    }
}
```

### Comparison operators
To check one thing is the same as another, use `thing1` `=` `thing2`.
Same can be down for greater `<`, grater than or equal `<=`, less than `>` and less than or equal `>=`.

### logical operators
The keyword `and` checks both conditions (left and right side of it) are true, and returns true, else false.

The keyword `or` checks checks either condition (left and right side of it) is true, and returns true if one or both are, else false.

The keyword `not` negatives the comparison, so `if not i = 3` will check `i` is not `3` instead of checking it is. 

## Label and jump

A label can be used to jump to a specific section of the program. They are defined by writing `label <label name>:` and are local to that script file.

Labels can be jumped to using the `jump` keyword followed by the label to jump to.

Label and jump example:

```lisp
label my_label:
; my label
```
```lisp
jump my_label ; jump to the label
```

## Mathematical operations
`/` to divide, `+` to add, `*` to multiply, `-` to subtract and `%` to get the module.

## Lists
Lists come in two types, dynamic and fixed.

Fixed size lists have a fixed size however are more performant than the dynamic list.


Lists can have their values changed via `my_list[index] := value` or via `my_list := [value, value, etc.]`. However, for fixed size, it is recommended to assign each value (former) as in the latter, you may get the size wrong.

Lists are indexed at zero, to get a value from the top of the list, use -1 and so on.

### Fixed
To create a fixed size list, you can specify the size of it or pass in what it needs to store (the values can change but the size cannot)

```lisp
i8[2] i1 ; create a list of i8's with a size of two
i8[] i2 := [10, 23] ; creates a list of i8's of the size two, assigning it the values 10 and 23 (for index 0 and 1 respectively)
```

### Dynamic
To create a dynamic list, there is only one way, create a list using `[]` without a number and do not assign anything to it when doing so, else it will be be a fixed size list.

```lisp
i8[] i3 ; create a dynamic list
i3[0] := -1 ; list of size 1
i3 := [10, 34, 24] ; list of size 3
```

## Custom data types
Custom datatypes, like variables, are scoped to where they are defined. They are defined by typing the keyword `datatype` followed by the name of the data.

For example, a custom position datatype

```lisp
datatype position {
    f64 x := 0
    f64 y := 0
    f64 z := 0
    const f64[3] start
}
```

You can then access a property of this datatype with `<datatype name>.<value>`. e.g. `position.x := 10`

To use it, type `<datatype name> <variable name>` like any other variable.
