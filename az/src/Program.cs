using System;
using Az.Tokenisation;

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
            lexer.Lex(@"./test/main.oskar");
        }
    }
}
