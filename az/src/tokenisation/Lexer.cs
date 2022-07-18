using System;
using Az.Tokenisation;

namespace Az.Tokenisation
{
    public class Lexer
    {
        public void Lex(string sourcefile)
        {
            // Mode
            Mode mode = Mode.Code;

            // Tokens list
            List<Token> tokens = new List<Token>();

            // Current token
            Token token = new Token();

            // Load tokens from files
            string[] keywords = System.IO.File.ReadAllLines("tokens/keywords.txt"); // Keywords
            string[] datatypes = System.IO.File.ReadAllLines("tokens/datatypes.txt"); // Datatypes
            string[] access = System.IO.File.ReadAllLines("tokens/access.txt"); // Access modifiers
            string[] mutability = System.IO.File.ReadAllLines("tokens/mutability.txt"); // Mutability modifiers
            string[] logicalOperators = System.IO.File.ReadAllLines("tokens/logical_operators.txt"); // Logical operators

            // Open file and read text
            string text = System.IO.File.ReadAllText(sourcefile);

            for (int i = 0; i < text.Length; i++)
            {
                Console.Write(text[i]);
            }

            // Loop through text
            for (int i = 0; i < text.Length; i++)
            {
                // Current character
                char c = text[i];

                switch (mode)
                {
                    case Mode.Code:
                        // Enter number mode
                        if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9')
                        {
                            // mode = Mode.Number;
                            token = new Token();
                            token.Type = Token.TokenType.Literal;
                            token.Value = "";
                            var dotCount = 0;
                            // FIXME: Prevent from crashing at end of line
                            while (Char.IsDigit(text[i]) || text[i] == '.' && i < text.Length - 1)
                            {
                                if (text[i] == '.')
                                {
                                    dotCount++;
                                }
                                if (dotCount > 1)
                                {
                                    Console.WriteLine("Error: Too many dots in number"!);
                                    // FIXME: Error handling
                                    break;
                                }
                                token.Value += text[i];
                                i++;
                            }
                            if (token.Value[token.Value.Length - 1] == '.')
                            {
                                // FIXME: Error handling
                                // token.Value = token.Value.Substring(0, token.Value.Length - 1);
                                Console.WriteLine("Error: Missing digit after dot!");
                                break;
                            }
                            tokens.Add(token);
                        }
                        // Enter string mode
                        if (text[i] == '"')
                        {
                            token = new Token();
                            token.Type = Token.TokenType.Text;
                            token.Value = "";
                            i++;
                            // FIXME: Add support for escape sequences
                            // FIXME: Prevent from crashing at end of line
                            while (text[i] != '"' && i < text.Length - 1)
                            {
                                token.Value += text[i];
                                i++;
                            }
                            tokens.Add(token);
                        }
                        // Separator
                        else if (text[i] == ',' || text[i] == '(' || text[i] == ')' || text[i] == '[' || text[i] == ']' || text[i] == '{' || text[i] == '}')
                        {
                            token = new Token();
                            token.Type = Token.TokenType.Separator;
                            token.Value = text[i].ToString();
                            tokens.Add(token);
                        }
                        // Comparison operators
                        else if (text[i] == '<' || text[i] == '>' || text[i] == '=')
                        {
                            string op = text[i].ToString();
                            if (op == "<" || op == ">")
                            {
                                if (i < text.Length - 1)
                                {
                                    if (text[i + 1] == '=')
                                    {
                                        op += "=";
                                        i++;
                                    }

                                }
                            }
                            token = new Token();
                            token.Type = Token.TokenType.ComparisonOperator;
                            token.Value = op.ToString();
                            tokens.Add(token);
                        }
                        // Assignment
                        else if (text[i] == ':')
                        {
                            string op = text[i].ToString();
                            if (op == ":")
                            {
                                if (i < text.Length - 1)
                                {
                                    if (text[i + 1] == '=')
                                    {
                                        op += "=";
                                        i++;
                                        token = new Token();
                                        token.Type = Token.TokenType.Operator;
                                        token.Value = op.ToString();
                                        tokens.Add(token);
                                    }

                                }
                            }
                        }
                        // Assignment
                        else if (text[i] == '-')
                        {
                            string op = text[i].ToString();
                            if (op == "-")
                            {
                                if (i < text.Length - 1)
                                {
                                    if (text[i + 1] == '>')
                                    {
                                        op += ">";
                                        i++;
                                        token = new Token();
                                        token.Type = Token.TokenType.Symbols;
                                        token.Value = op.ToString();
                                        tokens.Add(token);
                                    }

                                }
                            }
                        }
                        // Operators
                        else if (text[i] == '+' || text[i] == '-' || text[i] == '*' || text[i] == '/' || text[i] == '%')
                        {
                            token = new Token();
                            token.Type = Token.TokenType.Operator;
                            token.Value = text[i].ToString();
                            tokens.Add(token);
                        }
                        // Skip whitespace
                        else if (text[i] == ' ' || text[i] == '\n' || text[i] == '\t')
                        {
                            // Do nothing
                        }
                        else if (Char.IsLetter(c) || c == '_')
                        {
                            // FIXME: Crash when keyword at the end of the file (no space only)
                            token = new Token();
                            token.Type = Token.TokenType.Identifier;
                            token.Value = c.ToString();
                            while (Char.IsLetterOrDigit(text[i + 1]) && i < text.Length - 1)
                            {
                                token.Value += text[i + 1];
                                i++;
                            }
                            // Check if token is a keyword
                            if (keywords.Contains(token.Value)) token.Type = Token.TokenType.Keyword;
                            else if (datatypes.Contains(token.Value)) token.Type = Token.TokenType.Datatype;
                            else if (access.Contains(token.Value)) token.Type = Token.TokenType.Access;
                            else if (mutability.Contains(token.Value)) token.Type = Token.TokenType.Mutability;
                            else if (logicalOperators.Contains(token.Value)) token.Type = Token.TokenType.LogicalOperator;

                            tokens.Add(token);

                        }
                        else if (c == ';')
                        {
                            token = new Token();
                            token.Type = Token.TokenType.Comment;
                            token.Value = "";
                            i++;
                            // FIXME: Crash when comment at the end of the file (unless it's a newline)
                            while (text[i] != '\n' && i < text.Length)
                            {
                                token.Value += text[i];
                                i++;
                            }
                            tokens.Add(token);
                        }
                        break;

                    default:
                        Console.WriteLine("Unknown mode!");
                        break;
                }
            }

            var string_tokens = "";
            // Print tokens
            foreach (Token t in tokens)
            {
                var string_token_current = $"{t.Type} <;;> {t.Value}";
                string_tokens += string_token_current + "\n";
                Console.WriteLine($"{t.Type}:\t{t.Value}");
            }

            // Write to file
            System.IO.File.WriteAllText($"{sourcefile}.knot", string_tokens);
        }
    }
}