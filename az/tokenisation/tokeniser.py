from tokenisation.utils import GetTokenForSemanticSeparator
from tokenisation.utils import IsValidName
from tokenisation.utils import tokenPrevious
from tokenisation.utils import tokenNext
from tokenisation.utils import writeTokens
from tokenisation.utils import ReturnCharacter
from tokenisation.utils import GetPositionOfNextCharacter
from tokenisation.tokens import *
import tokenisation.tokens

# Language mode
context_global = "global"
context = context_global
context_history = [context]

context_string = "string"
context_comment_single = "comment_single"
context_comment_multi = "comment_multi"
context_clear_previous = "clear_previous"

# def change_scope(scope):
#     global context
#     if scope == "context_clear_previous":
#         context_history.pop()
#     else:
#         context_history.append(scope)
#     context = context_history[-]

def language_set_mode(mode):
    print(f"Setting language mode to {mode}")
    global context
    context = mode

def wordComplete(word):
    # And token
    if word == and_:
        return and_token
    # Or token
    elif word == or_:
        return or_token
    # If token
    elif word == if_:
        return if_token
    # Else token
    elif word == else_:
        return else_token
    # Else if token
    elif word == else_if:
        return else_if_token
    # Csharp keyword
    elif word == csharp:
        return csharp_token
    # Return keyword
    elif word == return_:
        return return_token
    # For keyword
    elif word == for_loop:
        return for_loop_token
    # While keyword
    elif word == while_loop:
        return while_loop_token
    # Lp keyword
    elif word == lp_loop:
        return lp_loop_token
    # break
    elif word == break_:
        return break_token
    # continue
    elif word == continue_:
        return continue_token
    # switch
    elif word == switch:
        return switch_token
    # case
    elif word == case:
        return case_token


    # Data types
    # Function
    elif word == function:
        return function_token
    # Void
    elif word == void:
        return void_token
    # String
    elif word == string:
        return string_token
    # Character
    elif word == character:
        return character_token
    # Number
    elif word == number:
        return number_token
    # Boolean
    elif word == boolean:
        return boolean_token
    # True
    elif word == true:
        return true_token
    # False
    elif word == false:
        return false_token
    # Null
    elif word == null:
        return null_token
    # uint64
    elif word == uint64:
        return uint64_token
    # int64
    elif word == int64:
        return int64_token
    # uint32
    elif word == uint32:
        return uint32_token
    # int32
    elif word == int32:
        return int32_token
    # uint16
    elif word == uint16:
        return uint16_token
    # int16
    elif word == int16:
        return int16_token
    # uint8
    elif word == uint8:
        return uint8_token
    # int8
    elif word == int8:
        return int8_token
    # float64
    elif word == float64:
        return float64_token
    # float32
    elif word == float32:
        return float32_token
    # infer
    elif word == infer:
        return infer_token
    # Const
    elif word == constant:
        return constant_token

    
    # Return unknown token
    return f"@{word}@"

def loopSourceAndGenerateTokens(source):
    global context
    iteration = 0
    word = ""
    while iteration < len(source):
        # Get the character
        character = ReturnCharacter(source, iteration)

        # String language mode - extract string from quotes
        if context == context_string:
            iteration += 1
            if character == quote:
                language_set_mode(context_global)
                yield f"@STRING@{word}@STRING_END@"
                word = ""
            else:
                word += character
            continue

        # Enter string language mode
        if character == quote:
            # Change to string mode
            language_set_mode(context_string)
            iteration += 1
            continue

        # Skip whitespace
        if character == "\t":
            iteration += 1
            continue

        # Add character to word, if valid
        if IsValidName(character):
            word += character
            iteration += 1
            if iteration < len(source):
                if not IsValidName(source[iteration]):
                    yield wordComplete(word)
                    word = ""
            continue

        # Get the token for the character
        token = GetTokenForSemanticSeparator(character)
        if (token != "INVALID"):
            yield token
        else:
            data = f"@{word}@"
            if data != "@@":
                yield data

        # Reset word
        word = ""

                
        
        # print(token)
        iteration += 1

def tokeniser(source):
    writeTokens(loopSourceAndGenerateTokens(source))