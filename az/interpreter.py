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