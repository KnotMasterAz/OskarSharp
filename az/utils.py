def writeTokens(args):
    with open("tokens.txt", "w") as f:
        for token in args:
            f.write(token + " ")

def tokenPrevious(tokens, index):
    return tokens[index - 1]

def tokenNext(tokens, index):
    return tokens[index - 1]