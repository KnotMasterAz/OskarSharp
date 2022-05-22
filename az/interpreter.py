from templates import Templates # Language templates
from code_generators.generate_csharp import code_generation # C# code generator

from tokenisation.tokeniser import tokeniser

# Source files
sourcefile = "test.az"
source = ""
tokenised_source = ""



# Generate code
def build_code():
    code_generation()



with open(sourcefile, "r") as f:
    # read file contains
    source = f.read()

    # Tokenize
    tokeniser(source)

    # Build code
    build_code()