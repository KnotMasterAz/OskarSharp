from templates import Templates # Language templates
from code_generators import generate_csharp # C# code generator

from tokenisation.tokeniser import tokeniser

# Source files
sourcefile = "test.az"
source = ""
tokenised_source = ""



# Generate code
def build_code(tokens):
    generate_csharp(tokens)



with open(sourcefile, "r") as f:
    # read file contains
    source = f.read()

    # Tokenize
    tokeniser(source)