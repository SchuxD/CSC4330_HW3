import re

# Define regular expressions for each token type
TOKEN_PATTERNS = {
    'ADD_OP': r'\+',
    'SUB_OP': r'-',
    'MUL_OP': r'\*',
    'DIV_OP': r'/',
    'MOD_OP': r'%',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'ASSIGN_OP': r'=',
    'EQ_OP': r'==',
    'LT_OP': r'<',
    'LTE_OP': r'<=',
    'GT_OP': r'>',
    'GTE_OP': r'>=',
    'AND_OP': r'&&',
    'OR_OP': r'\|\|',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'FLOAT_LITERAL': r'\d+\.\d+',
    'INT_LITERAL': r'\d+',
}

# Compile regular expressions into a dictionary of compiled patterns
TOKEN_PATTERNS_COMPILED = {token_type: re.compile(pattern) for token_type, pattern in TOKEN_PATTERNS.items()}

def tokenize(expression_str):
    for match in re.finditer('|'.join(TOKEN_PATTERNS_COMPILED.values()), expression_str):
        token_type = next(token_type for token_type, pattern in TOKEN_PATTERNS_COMPILED.items() if pattern is not None and pattern.match(match.group()))
        token_value = match.group(token_type)
        if token_type == 'INT_LITERAL':
            token_value = int(token_value)
        elif token_type == 'FLOAT_LITERAL':
            token_value = float(token_value)
        yield (token_type, token_value)
