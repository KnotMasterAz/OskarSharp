// Data types
i8
i16
i32
i64
u8
u16
u32
u64
f32
f64
bool
str

// int, uint, float default to 64 bits

// Assignment operator: :=

// Variables
const // Constant

// Scope
pub // Accessible from outside of the current directory (public) (default)
priv // Accessible only from within the current directory (private)

// Procedure specefic types
my_proc() // Invocation
pure // no side effects

priv i8 add i8 a, i8 b {
    ret a + b
}

// Events (scopeless procedures with no return value or arguments, cleared afrer each invocation)
fire my_signal // Invocation
event triggered_event {
    triggered_event(i32)
}

// Loops
forever {
    quit
}

while false = true {
    quit
}

for i8 i = 0; i < 10; i++ {
    print(i)
}

// Control flow
quit // Exit the context of the current procedure/loop/event
top // Return to the top of the context of the current procedure/loop/event

lable test_label {
    goto test_label
}

// Conditions
if i = 0 {
    print("true")
} elif i == 10 {
    print("false")
} finally {
    print("else")
}

case my_var {
    when 1 {}
    when 2 {}
    when 3 {}
    when 4,5,6 {}
    else {}
}

// lists (static)
i8[] my_list = [1,2,3,4,5]
i8[7] my_list

// lists (dynamic)
i8[] my_list = []
my_list[0] = 1

// Code generation
@replace("my_var", "my_var2")
@set(VARIABLE_PREPROCESSOR, "my_var")
@replace(VARIABLE_PREPROCESSOR, "my_var2")
@expand("i", "i64")
@expand("u", "u64")
@expand("f", "f64")
@expand("b", "bool")
@expand("s", "str")

@lable MY_TEST
@goto MY_TEST if VARIABLE_PREPROCESSOR = "my_var2"
@copy test.oskar to test.oskar.bak
@move test.oskar to test.oskar.bak
@delete test.oskar.bak
@rename test.oskar.bak to test.oskar
@paste test.oskar.bak to test.oskar
@paste test.oskar to test.oskar.bak at label MY_TEST
@paste test.oskar to test.oskar.bak at label here

@compile test.oskar
@compile project.oskar