namespace Az.Tokenisation
{
    internal struct Token
    {
        public TokenType Type;
        public string Value;
        public enum TokenType
        {
            Identifier,
            Datatype,
            Keyword,
            Literal,
            Operator,
            Separator,
            Comment,
            Text,
            Access,
            Mutability,
            LogicalOperator,
            ComparisonOperator,
            Symbols,
        }
    }
}