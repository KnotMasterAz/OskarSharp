import sys # Import system module

language_mode = "code"
variable_count = 0
variable_values = []
variable_names = []

if sys.argv.__len__() < 2:
    print("Usage: python3 runner.py <file>")
    exit(1)

# Open the tokens file
with open(sys.argv[1], "r") as f:
    # Print token file contents
    print(f.read())

    # Entering interpreter
    print("Entering interpreter...")

    # Iteration counter
    i = 0

    # Loop through reach line
    for line in f:
        # Print the iteration counter
        print("Iteration: " + str(i))

        if language_mode == "type_found":
            variable_names[variable_count] = line.replace("@IDENTIFIER@", "")
            language_mode = "type_value_needed"
        elif language_mode == "type_value_needed":
            variable_values[variable_count] = line.replace("@IDENTIFIER@", "")
            language_mode = "code"

        if line.startswith("NUMBER"):
            language_mode = "type_found"
            variable_count += 1
            continue

        # Print the iteration counter
        print("Iteration: " + str(i))

        if line.startswith("@IDENTIFIER@"):
            print("Find an identifier: " + line.replace("@IDENTIFIER@", ""))
            continue