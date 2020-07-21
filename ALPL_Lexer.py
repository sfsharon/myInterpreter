#!/usr/bin/env python

"""
ALPL_Lexer - A simple lexer implementation for the ALPL language, built for myInterpreter 
Code based on https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1
"""

import sys
import re

# Tags for the ALPL language
RESERVED = 'RESERVED'   # Reserved word
INT      = 'INT'        # Integer
LABEL    = 'LABEL'      # Label string used for jumping
REG      = 'REG'        # Register string (R0 - R9)

# Token expressions
token_exprs = [
    (r'[ \n\t]+',                   None),          # Blanks - Have no token
    (r'#[^\n]*',                    None),          # Remarks (python style) - Have no token
    (r'\:=',                        RESERVED),      # Assignment operator 
    (r'LET',                        RESERVED),      # Command reserved word
    (r'IF',                         RESERVED),      # Command reserved word
    (r'JUMP',                       RESERVED),      # Command reserved word
    (r'CALL',                       RESERVED),      # Command reserved word
    (r'RETURN',                     RESERVED),      # Command reserved word
    (r'PRINT',                      RESERVED),      # Command reserved word
    (r'[A-Za-z][A-Za-z0-9_]*\:',    LABEL),         # Label is an alphanumeric string, followed by a colon
    (r'[0-9]+',                     INT),           # Integer token - 
                                                    # TODO - Deal with negative integer
    (r'R[0-9]+',                    REG)            # Register token : R0 - R9
    ]

    
def lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: "%s"' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


if __name__ == "__main__" :
    exampleFile_1 = r"./examples/countTo10.alpl"
    exampleFile_2 = r"./examples/print2020.alpl"
    
    file = open(exampleFile_1)
    characters = file.read()
    file.close()
    tokens = lex(characters)
    for token in tokens:
        print (token)