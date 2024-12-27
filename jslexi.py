import re

# Define the token specifications
TOKEN_SPECIFICATION = [
    ('NUMBER',    r'\d+(\.\d*)?'),           # Integer or decimal number
    ('IDENTIFIER', r'[A-Za-z_]\w*'),         # Variable/function names
    ('OPERATOR',  r'[+\-*/=<>!]'),           # Arithmetic/Comparison operators
    ('STRING',    r'"[^"]*"|\'[^\']*\''),    # Double or single-quoted strings
    ('COMMENT',   r'//.*|/\*[\s\S]*?\*/'),   # Single-line or multi-line comments
    ('WHITESPACE', r'[ \t\n]+'),             # Whitespace (spaces, tabs, newlines)
    ('SYMBOL',    r'[{}()[\],.;]'),          # Symbols like braces, parentheses
]

class LexicalAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        # Compile the regex patterns into a single pattern
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
        for match in re.finditer(token_regex, self.source_code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE' and kind != 'COMMENT':
                self.tokens.append((kind, value))

    def display_tokens(self):
        print("Tokens:")
        for token in self.tokens:
            print(token)

def main():
    # Prompt user for JavaScript code input
    print("Enter your JavaScript code (end with an empty line):")
    
    # Read multiple lines of input until an empty line is entered
    source_code = []
    while True:
        line = input()
        if line.strip() == "":
            break
        source_code.append(line)
    
    # Join the lines into a single string
    complete_code = "\n".join(source_code)

    # Create a lexical analyzer instance and tokenize the JavaScript code
    analyzer = LexicalAnalyzer(complete_code)
    analyzer.tokenize()
    analyzer.display_tokens()

if __name__ == "__main__":
    main()
