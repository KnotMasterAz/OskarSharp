#!/usr/bin/env python

import os
import sys
import shutil

'''
#import token

# tokens = []
# mode_current = None

# mode_keyword = -1
# mode_type = -2

# token_position = 0

# token_count = 0


# def token_offset_is(offset, token_type):
#     if token_type == tokens[token_count+offset]:
#         return True
#     return False
    
# def token_next(token_to_check):
#     return token_offset_is(1, token_to_check)
'''

def log(message):
    if log_to_console:
        print(message)

def clean_up():
    # Remove the tmp and output directory if they exist
    shutil.rmtree("output/", ignore_errors=True) # delete old output
    shutil.rmtree("tmp/", ignore_errors=True) # delete tmp

def line_add_semi_colon_non_function(text):
    text = text.replace("\n", "")
    if text[-1:].isalpha():
        return True
    elif text[-1:].isnumeric():
        return True
    return False

def validate_version(file):
    with open(file, "r") as f:
        v = f.readline()
        version = v
        if version.startswith("//V"):
            version = version.replace("//V", "")
            version = version.replace("+", "")
            version = version.replace("\n", "")
            v_num = int(version.replace(".", ""))

            if version_num < v_num:
                if not (force_compile_with_version):
                    print(f"FATAL ERROR: Transpiler too old!\nAborting transpile!")
                    print(f"Version mismatch!")
                    print(f"Expected: {version}")
                    print(f"Found: {version_string}")
                    exit(1)
                else:
                    log("WARNING: Version mismatch! Forcing compile!")

def template_generate(run=False, file="hello", template="Console", script_name="ConsoleApp", namespace_non_console="KnotsSharp", inherit="MonoBehaviour", app_name="Out"):
    # Clean up
    clean_up()


    # Discord tabbing in when no template is used
    tabbed = True
    if (template == "CodeBlock"):
        tabbed = False

    # Transpile code
    code = transpile(f"code/{file}.knots", tab=tabbed) # Finds and replaces without caring about context most of the time (token/parser should be used)

    # Templates
    if template == "CodeBlock":
        # Generate directory structure
        os.makedirs("output", exist_ok=True)
        os.chdir('output')

        # Generate the script template and populate it with the contents of the knots file
        with open(f"{script_name}.cs", "w") as f:
            f.write(f"{code}\n")
            
    elif template == "Console":
        # Generate directory structure
        os.makedirs("output", exist_ok=True)
        os.chdir('output')
        os.system(f"dotnet new Console -n {app_name}")
        os.chdir(f"{app_name}")

        # Generate the script template and populate it with the contents of the knots file
        with open("Program.cs", "w") as f:
            f.write("using System;\n\n");
            f.writelines(f"namespace {script_name}\n")
            f.write("{\n")
            f.write("\tinternal class Program\n")
            f.write("\t{\n")
            f.write(f"{code}\n")
            f.write("\t}\n")
            f.write("}\n")
        
        # Build
        os.system("dotnet build")

        # Run
        if run:
            os.system("dotnet run")

    elif template == "Unity":
        # Generate directory structure
        os.makedirs(f"output/{namespace_non_console}", exist_ok=True)
        shutil.copyfile("transpiler2.0/templates/Unity/Signal.cs", f"output/{namespace_non_console}/Signal.cs")
        os.chdir(f'output/{namespace_non_console}')

        # generate the script template and populate it with the output of the knots file
        with open(f"{script_name}.cs", "w") as f:
            f.write("using UnityEngine;\n")
            f.write("using System.Collections;\n")
            f.write("using KnotsSharp;\n\n")
            f.write(f"namespace {namespace_non_console}\n")
            f.write("{\n")
            f.write(f"\tpublic class {script_name} : {inherit}\n")
            f.write("\t{\n")
            f.write(f"{code}\n")
            f.write("\t}\n")
            f.write("}\n")
    else:
        print("Template not found!")
        print("Run --help for more")
        # Abort
        exit(1)

def transpile(file, tab=True):
    # Check file exists
    if not os.path.exists(file):
        print("FATAL ERROR: file does not exist in code directory!\nAborting transpile!")
        exit(1)

    validate_version(file)

    with open(file, "r") as f:
        output = ""
        for line in f:
            # Unity signals
            line = line.replace("unity_add_signal", "Signal.Instance.AddSignal")
            line = line.replace("unity_remove_signal", "Signal.Instance.RemoveSignal")
            line = line.replace("unity_signal_destroy", "Signal.Instance.SignalDestroyAll")
            line = line.replace("unity_signal_exists", "Signal.Instance.SignalExists")

            # Unity generic
            line = line.replace("unity_print", "Debug.Log")

            # input += line
            line = line.replace("number", "double")
            line = line.replace("generic<Type>", "T")
            line = line.replace("<Type>", "<T>")
            line = line.replace("fun main()", "void Main(string[] args)")
            line = line.replace("fun", "void")
            line = line.replace(".length", ".Length")
            line = line.replace("print_online", "Console.Write")
            line = line.replace("print", "Console.WriteLine")
            line = line.replace("read", "Console.ReadLine")
            line = line.replace("fun:", "static ")
            line = line.replace("csh.", "")

            # More data types
            # Unsigned
            line = line.replace("uint64", "ulong")
            line = line.replace("uint32", "uint")
            line = line.replace("uint16", "ushort")
            line = line.replace("uint8", "byte")
            # Signed
            line = line.replace("int64", "long")
            line = line.replace("int32", "int")
            line = line.replace("int16", "short")
            line = line.replace("int8", "sbyte")
            # Floats
            line = line.replace("float64", "double")
            line = line.replace("float32", "float")
            # Auto infer type
            line = line.replace("infer", "var")

            if (auto_semicolon):
                # Automatically add semi-colon after ) at the end of a line
                if line.endswith(")\n"):
                    line = line.replace(")\n", ");\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after ' at the end of a line
                if line.endswith("'\n"):
                    line = line.replace("'\n", "';\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after + at the end of a line
                if line.endswith("+\n"):
                    line = line.replace("+\n", "+;\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after - at the end of a line
                if line.endswith("-\n"):
                    line = line.replace("-\n", "-;\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after * at the end of a line
                if line.endswith("*\n"):
                    line = line.replace("*\n", "*;\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after / at the end of a line
                if line.endswith("/\n"):
                    line = line.replace("/\n", "/;\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after " at the end of a line
                if line.endswith("\"\n"):
                    line = line.replace("\"\n", "\";\n")
                    log(f"Added termination to end of line automatically:\n{line}")

                # Automatically add semi-colon after a character (a-Z) at the end of a line
                if (line_add_semi_colon_non_function(line)):
                    line = line.replace("\n", ";\n")
                    log(f"Added termination to end of line automatically:\n{line}")

            # Add tabs
            if (tab):
                output += "\t\t"
            
            # Add line to the output
            output += f"{line}"
    
    # Return the output
    return output

if __name__ == "__main__":
    
    output = ""
    input = "" 
    log_to_console = False
    auto_semicolon = True
    run_after_build = False
    force_compile_with_version = False

    version_numerical = [0, 2, 1]
    version_string = f"{version_numerical[0]}.{version_numerical[1]}.{version_numerical[2]}";
    version_num = int(f"{version_numerical[0]}{version_numerical[1]}{version_numerical[2]}");

    log("Version: " + version_string);

    # Run
    if "--help" in sys.argv:
        print("Usage: source (in \"code\" directory, no extension - \"hello\")* [--Unity, --Console, --CodeBlock]* [--help] [--log] [--run] [--clear-old] [--no-auto-semicolon] [--force-compile]")
        exit(0);

    # Clean up old files
    if "--clear-old" in sys.argv:
        clean_up()
        exit(0)

    # File to build
    if sys.argv.__len__() > 1:
        file_to_build = sys.argv[1]
    else:
        print("FATAL ERROR: No file specified!\nAborting transpile!")
        exit(1)

    # Force compile with version
    if "--force-compile" in sys.argv:
        force_compile_with_version = True

    # Run
    if "--run" in sys.argv:
        run_after_build = True

    # Auto-semi disable
    if "--no-auto-semicolon" in sys.argv:
        auto_semicolon = False

    # Template
    if "--Unity" in sys.argv:
        template_to_use = "Unity"
        if (run_after_build):
            print("Ignoring --run flag, as it is not compatible with the Unity template.")
    elif "--CodeBlock" in sys.argv:
        template_to_use = "CodeBlock"
        if (run_after_build):
            print("Ignoring --run flag, as it is not compatible with the CodeBlock template.")
    elif "--Console" in sys.argv:
        template_to_use = "Console"
    else:
        # Abort no template specified
        print("FATAL ERROR: No template specified!\nAborting transpile!")
        exit(1)

    # Run
    if "--log" in sys.argv:
        log_to_console = True
    else:
        log_to_console = False

    # Build
    template_generate(run=run_after_build, file=file_to_build, template=template_to_use, script_name=file_to_build, namespace_non_console="KnotsSharp", inherit="MonoBehaviour", app_name=file_to_build)
