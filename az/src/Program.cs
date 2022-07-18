using System;
using Az.Tokenisation;

namespace Az
{
    class Program
    {
        static void Main(string[] args)
        {
            Lexer lexer = new Lexer();
            lexer.Lex(@"./test/main.oskar");
        }
    }
}
