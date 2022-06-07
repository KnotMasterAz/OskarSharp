import sys
from tokenisation.utils import writeTokens
from tokenisation.tokeniser import loopSourceAndGenerateTokens # Import system

from templates import Templates # Language templates
from code_generators.generate_csharp import code_generation # C# code generator

from tokenisation.tokeniser import tokeniser # Import tokeniser

if sys.argv.__len__() < 2:
    print("Usage: python3 interpreter.py <file>")
    exit(1)

# Source files
sourcefile = sys.argv[1]
source = ""
tokenised_source = ""

# Generate code
def build_code():
    code_generation()

def live_code_translation():
    print("Type 'exit' to quit!")
    while True:
        val = input(">>> ")
        if val == "exit":
            break
        else:
            tokenised_source_generator = loopSourceAndGenerateTokens(val)
            writeTokens(tokenised_source_generator)
            tokenised_source = ""
            for token in tokenised_source_generator:
                tokenised_source += token + ", "
            print("\n\n")
            print(f"Tokens:\n{tokenised_source}")
            print("\n\nC# code:")
            build_code()

if (sys.argv[1] == "--live"):
    live_code_translation()
    exit(0)

with open(sourcefile, "r") as f:
    # read file contains
    source = f.read()

    # Tokenize
    tokeniser(source)

    # Build code
    build_code()