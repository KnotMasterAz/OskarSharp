// #define CHAOS_MODE

using System;
using Az.Tokenisation;
#if CHAOS_MODE
using Experimental.Csharp;
#endif

namespace Az
{
    class Program
    {
        static void Main(string[] args)
        {
            // Check if the user provided a file to parse
            if (args.Length == 0)
            {
                Console.WriteLine("Usage: Az.exe <file>");
                return;
            }
            // Check the file exists, and if not, exit.
            if (!System.IO.File.Exists(args[0]))
            {
                Console.WriteLine("File not found: " + args[0]);
                return;
            }

            // Create a new tokeniser and parse the file.
            Lexer lexer = new Lexer();
            lexer.Lex(args[0]);

            Console.WriteLine("STATE:: LEXING HAS FINISHED!");

            #if CHAOS_MODE
            Generator generator = new Generator();
            generator.Generate($"{args[0]}.knot");
            #endif
        }
    }
}

#if CHAOS_MODE
namespace Experimental.Csharp
{
    internal class Generator
    {
        public void Generate(string knot)
        {
            string output = "";

            string[] tokens = System.IO.File.ReadAllLines(knot); // Datatypes

            var tabbing = 0;

            // Loop through each line of the file.
            foreach (string line in tokens)
            {
                // Split the line into tokens.
                string[] tokens2 = line.Split(" <;;> ");

                if (tokens2[0] == "Datatype") output += $"{ConvertType(tokens2[1])} ";
                if (tokens2[0] == "Identifier") output += $"{tokens2[1]} ";
                // if (tokens2[0] == "Access") output += $"{ConvertAccess(tokens2[1])} ";
                // if (tokens2[0] == "Mutability") output += $"{ConvertMutability(tokens2[1])} ";
                if (tokens2[0] == "Separator") output += $"{ConvertSeparator(tokens2[1])} ";
                if (tokens2[0] == "Symbols") output += $"{ConvertSymbols(tokens2[1])} ";
                if (tokens2[0] == "Literal") output += $"{tokens2[1]} ";
                if (tokens2[0] == "Operator") output += $"{ConvertOperator(tokens2[1])} ";
                if (tokens2[0] == "Text") output += $"\"{tokens2[1]}\" ";
                if (tokens2[0] == "Comment") output += $"//{tokens2[1]}\n";
                if (tokens2[0] == "Keyword") output += $"{ConvertKeyword(tokens2[1])} ";
            }
            Console.WriteLine(output);

            string code = "namespace Test\n{\n    class Program\n    {\n        static void Main(string[] args)\n        {\n            main(args.ToString());\n        }\n        __GEN__\n    }\n}";

            // Replace the __GEN__ tag with the generated code.
            code = code.Replace("__GEN__", output);

            System.IO.File.WriteAllText(@"./test/main.oskar.cs", code);
        }
        private string ConvertType(string type)
        {
            // Convert the type to a C# type.
            if (type == "u8")  return "byte";
            if (type == "u16") return "ushort";
            if (type == "u32") return "uint";
            if (type == "u64") return "ulong";
            if (type == "i8")  return "sbyte";
            if (type == "i16") return "short";
            if (type == "i32") return "int";
            if (type == "i64") return "long";
            if (type == "f32") return "float";
            if (type == "f64") return "double";
            if (type == "bool") return "bool";
            if (type == "str") return "string";
            if (type == "pure") return "void";

            return "";
        }
        private string ConvertSeparator(string type)
        {
            // This is gonna be hacky.
            if (type == ",") return ", ";
            if (type == "(") return "(";
            if (type == ")") return ");\n";
            if (type == "{") return ")\n{\n";
            if (type == "}") return "\n}";

            return "";
        }

        private string ConvertSymbols(string type)
        {
            // This is gonna be hacky.
            if (type == "->") return "(";

            return "";
        }

        private string ConvertOperator(string type)
        {
            // This is gonna be hacky.
            if (type == ":=") return "=";

            return "";
        }

        private string ConvertKeyword(string type)
        {
            // This is gonna be hacky.
            if (type == "if") return "if";
            if (type == "else") return "else";
            if (type == "while") return "while";
            if (type == "ret") return "return";

            return "";
        }
    }
}
#endif