from tokenisation.tokens import *

'''
    Please note this code generator is incomplete and will not work for all cases.
    This script only contains the basic functionality to generate code the code for the test script.
    The code generator will be expanded to include more functionality in the future however is not yet complete.
'''

code = ""
tab_size = ""

def code_generation():
    # Reset code to empty
    code = ""
    tab_size = ""

    # Python loop through and read each line in file
    with open("knot", "r") as f:
        for line in f:
            if line.startswith(function_token):
                code += function_lang + ""
                continue
            elif line.startswith(denote_token):
                code += denote_lang + " "
                continue
            elif line.startswith(l_param_token):
                code += l_param_lang
                continue
            elif line.startswith(r_param_token):
                code += r_param_lang
                continue
            elif line.startswith(l_brackets_token):
                code += l_brackets_lang
                continue
            elif line.startswith(r_brackets_token):
                code += r_brackets_lang
                continue
            elif line.startswith(l_curly_token):
                code += l_curly_lang + "@NEWLINE@"
                tab_size += "\t"
                continue
            elif line.startswith(r_curly_token):
                code += r_curly_lang + "@NEWLINE@"
                tab_size = tab_size[:-1]
                continue
            elif line.startswith("@IDENTIFIER@"):
                code += line.replace("@IDENTIFIER@", "")
                continue
            elif line.startswith("@STRING@"):
                code += "\"" + line.replace("@STRING@", "").replace("@STRING_END@", "") + "\""
                continue
            elif line.startswith(assign_token):
                code += f" {assign_lang} "
                continue
            elif line.startswith(assign_plus_token):
                code += " " + assign_plus_lang + " "
                continue
            elif line.startswith(minus_token):
                code += " " + minus_lang + " "
                continue
            elif line.startswith(mult_token):
                code += " " + mult_lang + " "
                continue
            elif line.startswith(plus_token):
                code += " " + plus_lang + " "
                continue
            elif line.startswith(pow_token):
                code += " " + pow_lang + " "
                continue
            elif line.startswith(mod_token):
                code +=" " +  mod_lang + " "
                continue
            elif line.startswith(div_token):
                code += " " + div_lang + " "
                continue
            elif line.startswith(termination_token):
                code += termination_lang + "@NEWLINE@"
                continue
            # trigger
            elif line.startswith(trigger_token):
                code += trigger_lang + " "
                continue
            # void
            elif line.startswith(void_token):
                code += void_lang + " "
                continue
            # float64
            elif line.startswith(float64_token):
                code += float64_lang + " "
                continue
            # float32
            elif line.startswith(float32_token):
                code += float32_lang + " "
                continue
            # int64
            elif line.startswith(int64_token):
                code += int64_lang + " "
                continue
            # int32
            elif line.startswith(int32_token):
                code += int32_lang + " "
                continue
            # int16
            elif line.startswith(int16_token):
                code += int16_lang + " "
                continue
            # int8
            elif line.startswith(int8_token):
                code += int8_lang + " "
                continue
            # uint64
            elif line.startswith(uint64_token):
                code += uint64_lang + " "
                continue
            # uint32
            elif line.startswith(uint32_token):
                code += uint32_lang + " "
                continue
            # uint16
            elif line.startswith(uint16_token):
                code += uint16_lang + " "
                continue
            # uint8
            elif line.startswith(uint8_token):
                code += uint8_lang + " "
                continue
            # string
            elif line.startswith(string_token):
                code += string_lang + " "
                continue
            # bool
            elif line.startswith(boolean_token):
                code += boolean_lang + " "
                continue
            # if
            elif line.startswith(if_token):
                code += if_lang + " "
                continue
            # else
            elif line.startswith(else_token):
                code += else_lang + " "
                continue
            # else if
            elif line.startswith(else_if_token):
                code += else_if_lang + " "
                continue
            # separators
            elif line.startswith(separators_token):
                code += separators_lang + " "
                continue
            # Return
            elif line.startswith(return_token):
                code += return_lang + " "
                continue
            # Constants
            elif line.startswith(constant_token):
                code += constant_lang + " "
                continue
            # Single line comments
            elif line.startswith("@COMMENT_SINGLE@"):
                code += comment_single_lang + line.replace("@COMMENT_SINGLE@", "") + "@NEWLINE@"
                continue

    # Add alias for console write to print
    code += f"\n\n static void print(string message) => Console.Write(message);"
    code = code.replace("\n", "").replace("@NEWLINE@", "\n")

    print(code)