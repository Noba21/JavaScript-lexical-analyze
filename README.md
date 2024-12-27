# README for Lexical Analyzer

## Project Title
Lexical Analyzer for JavaScript Code

## Overview
The **Lexical Analyzer** is a Python-based tool designed to perform lexical analysis on JavaScript code. It tokenizes input code to identify various elements such as keywords, identifiers, operators, strings, comments, whitespace, and symbols. This tool is useful for understanding the structure of JavaScript code and can serve as a foundational component for building more complex language processing tools.



## Technologies Used
- **Python 3.8+**: Programming language used for developing the lexical analyzer.
- **Regular Expressions (re)**: Python's built-in library for pattern matching and text manipulation.

## Features
- **Tokenization**: Analyzes JavaScript code and breaks it down into meaningful tokens.
- **User Input**: Allows users to input their own JavaScript code for analysis.
- **Token Display**: Outputs the identified tokens along with their types.

## Installation
1. **Clone the Repository**:
2. **Install Required Packages**:
   Ensure you have Python installed. No additional packages are required beyond the standard library.

3. **Run the Application**:
   Start the lexical analyzer:
 

## Usage
1. Run the script in your terminal:
2. When prompted, enter your JavaScript code line by line.
3. To finish inputting code, press `Enter` on an empty line.
4. The program will output the tokens generated from your JavaScript code.

### Example Input
```javascript
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        console.log("Even number: " + i);
    }
}
```

### Example Output
```
Tokens:
('IDENTIFIER', 'for')
('SYMBOL', '(')
('IDENTIFIER', 'let')
('IDENTIFIER', 'i')
('OPERATOR', '=')
('NUMBER', '0')
('SYMBOL', ';')
('IDENTIFIER', 'i')
('OPERATOR', '<')
('NUMBER', '10')
('SYMBOL', ';')
('IDENTIFIER', 'i')
('OPERATOR', '++')
('SYMBOL', ')')
('SYMBOL', '{')
...
```

