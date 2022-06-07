from tokenisation.tokens import *

def writeTokens(args):
    with open("knot", "w") as f:
        for token in args:
            f.write(f"{token}\n")

def tokenPrevious(tokens, index):
    return tokens[index - 1]

def tokenNext(tokens, index):
    return tokens[index - 1]

# Return true if name is valid
def IsValidName(character):
    if character.isalpha() or character.isnumeric() or character == "_":
        return True
    return False

def GetPositionOfNextCharacter(source, index):
    character = ""
    if index >= len(source):
        return -404

    while index < len(source) and not IsValidName(source[index]):
        character += source[index]
        index += 1

    return IsValidName(character)

def ReturnCharacter(source, index):
    return source[index]

# Mathematical operators
def GetTokenForMathematicalOperator(character):
    # Addition
    if (character == plus):
        return plus_token
    # Subtraction
    elif (character == minus):
        return minus_token
    # Multiplication
    elif (character == mult):
        return mult_token
    # Division
    elif (character == div):
        return div_token
    # Modulus
    elif (character == mod):
        return mod
    # Power
    elif (character == pow):
        return pow_token
    # Equals
    elif (character == assign):
        return assign_token

    # Return invalid token
    return "INVALID"

def GetTokenForSemanticSeparator(character):
    # Params
    # Left
    if (character == l_param):
        return l_param_token
    # Right
    elif (character == r_param):
        return r_param_token

    # Square Brackets
    elif (character == l_brackets):
        return l_brackets_token
    elif (character == r_brackets):
        return r_brackets_token
    
    # Curly Brackets
    elif (character == l_curly):
        return l_curly_token
    elif (character == r_curly):
        return r_curly_token
    
    # Denote type
    elif (character == denote):
        return denote_token
    
    # Termination
    elif (character == termination):
        return termination_token

    # Separator
    elif (character == separators):
        return separators_token

    # Return invalid token
    return "INVALID"