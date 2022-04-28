@staticmethod
class Tokens():
    # Parmas
    l_param = "("
    l_param_lang = "("
    r_param = ")"
    r_param_lang = ")"

    # Square Brackets
    l_brackets = "["
    l_brackets_lang = "["
    r_brackets = "]"
    r_brackets_lang = "]"

    # Curly Brackets
    l_curly = "{"
    l_curly_lang = "{"
    r_curly = "}"
    r_curly_lang = "}"

    # strings
    quote = "\""
    quote_lang = "\""
    escape_chr = "\\"
    escape_chr_lang = "\\"
    newline = "\n"
    newline_lang = "\n"
    string_format = "$"
    string_format_lang = "$"

    # operators
    plus = "+"
    plus_lang = "+"
    minus = "-"
    minus_lang = "-"
    mult = "*"
    mult_lang = "*"
    div = "/"
    div_lang = "/"
    mod = "%"
    mod_lang = "%"
    pow = "^"
    pow_lang = "^"
    assign = "="
    assign_lang = "="
    assign_plus = "+="
    assign_plus_lang = "+="
    assign_minus = "-="
    assign_minus_lang = "-="
    assign_mult = "*="
    assign_mult_lang = "*="
    assign_div = "/="
    assign_div_lang = "/="
    assign_mod = "%="
    assign_mod_lang = "%="
    not_equal = "!="
    not_equal_lang = "!="
    equal = "=="
    equal_lang = "=="
    negation = "not"
    negation_lang = "!"
    and_ = "and"
    and_lang = "&&"
    or_ = "or"
    or_lang = "||"
    greater = ">"
    greater_lang = ">"
    greater_equal = ">="
    greater_equal_lang = ">="
    less = "<"
    less_lang = "<"
    less_equal = "<="
    less_equal_lang = "<="

    # termination statement
    termination = ";"
    termination_lang = ";"

    # Comments (single line)
    comment_single = "//"
    comment_single_lang = "//"

    # Comments (multi line)
    comment_multi = "/*"
    comment_multi_lang = "/*"
    comment_multi_end = "*/"
    comment_multi_end_lang = "*/"

    # switch statement
    switch = "switch"
    switch_lang = "switch"
    case = "case"
    case_lang = "case"
    default = "default"
    default_lang = "default"

    # loops
    for_loop = "for"
    for_loop_lang = "for"
    while_loop = "while"
    while_loop_lang = "while"
    lp_loop = "lp"
    lp_loop_lang = "for"
    
    # continue and break
    continue_ = "continue"
    continue_lang = "continue"
    break_ = "break"
    break_lang = "break"

    # if statement
    if_ = "if"
    if_lang = "if"

    # C#
    csharp = "csh"
    csharp_lang = ""

    # seperator
    seperator = ","
    seperator_lang = ","

    # function keyword
    fun = "fun:"
    fun_lang = "static"

    # Generic data types

    # void
    void = "pure"
    void_lang = "void"

    # string
    string = "str"
    string_lang = "string"

    # character
    character = "chr"
    character_lang = "char"

    # num
    number = "num"
    number_lang = "double"

    # boolean
    bool = "bool"
    bool_lang = "bool"

    # true
    true = "true"
    true_lang = "true"

    # false
    false = "false"
    false_lang = "false"

    # null
    null = "nil"
    null_lang = "null"

    # More data types

    # Unsigned

    # uint64
    uint64 = "uint64"
    uint64_lang = "uint64"

    # uint32
    uint32 = "uint32"
    uint32_lang = "uint"

    # uint16
    uint16 = "uint16"
    uint16_lang = "ushort"

    # uint8
    uint8 = "uint8"
    uint8_lang = "byte"

    # Signed

    # int64
    int64 = "int64"
    int64_lang = "long"

    # int32
    int32 = "int32"
    int32_lang = "int"

    # int16
    int16 = "int16"
    int16_lang = "short"

    # int8
    int8 = "int8"
    int8_lang = "sbyte"

    # Floats

    # Float64
    float64 = "float64"
    float64_lang = "double"

    # Float32
    float32 = "float32"
    float32_lang = "float"

    # Auto infer type
    infer = "auto"
    infer_lang = "var"

    # spaces
    space = " "
    space_lang = " "

    # Return
    return_ = "ret"
    return_lang = "return"
