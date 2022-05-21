from templates import Templates
from tokens import Tokens

from utils import writeTokens

# Source files
sourcefile = "test.az"
source = ""

# Language mode
context = context_global = "global"
context_string = "string"
context_comment_single = "comment_single"
context_comment_multi = "comment_multi"

# Return true if the character is a semantic separator
def IsSpaceOrSemanticSeparator(character):
    if character == " " or character.isalpha() or character.isnumeric() or character == "_":
        return False
    return True

def loopThroughSourceFile(source):
    iteration = 0
    word = ""
    while iteration < len(source):
        if (IsSpaceOrSemanticSeparator(source[iteration])):
            yield word
            word = ""
        word += source[iteration]
        # print(token)
        iteration += 1

with open(sourcefile, "r") as f:
    source = f.read()
    # splitted_source = source.split("\n")
    writeTokens(loopThroughSourceFile(source))

def tokenPrevious(tokens, index):
    return tokens[index - 1]