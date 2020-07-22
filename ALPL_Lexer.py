#!/usr/bin/env python

"""
ALPL_Lexer - A simple lexer implementation for the ALPL language, built for myInterpreter 
Code based on https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1
"""

import sys
import re

# Tags for the ALPL language
RESERVED   = 'RESERVED'   # Reserved word
INT        = 'INT'        # Integer
LABEL      = 'LABEL'      # Label string used for jumping
REG        = 'REG'        # Register string (R0 - R9)
OP_ADD     = 'OP_ADD'
OP_MULT    = 'OP_MULT'
LABEL_ADDR = 'LABEL_ADDR'

# Token expressions
token_exprs = [
    (r'[ \n\t]+',                   None),          # Blanks - Have no token
    (r'#[^\n]*',                    None),          # Remarks (python style) - Have no token
    (r'\:=',                        RESERVED),      # Assignment operator 
    (r'\+',                         OP_ADD),      # Plus operator 
    (r'\*',                         OP_MULT),      # Multiplication operator 
    (r'>',                          RESERVED),      # Greater then Boolean operator
    (r'<',                          RESERVED),      # Less then Boolean operator
    (r'=',                          RESERVED),      # Equal Boolean operator
    (r'\bLET\b',                    RESERVED),      # Command reserved word, match only exact word
    (r'\bIF\b',                     RESERVED),      # Command reserved word, match only exact word
    (r'\bJUMP\b',                   RESERVED),      # Command reserved word, match only exact word
    (r'\bCALL\b',                   RESERVED),      # Command reserved word, match only exact word
    (r'\bRETURN\b',                 RESERVED),      # Command reserved word, match only exact word
    (r'\bPRINT\b',                  RESERVED),      # Command reserved word, match only exact word
    (r'[0-9]+',                     INT),           # Integer token 
                                                    # TODO - Deal with negative integer
    (r'R[0-9]+',                    REG),           # Register token : R0 - R9
    (r'[A-Za-z][A-Za-z0-9_]*\:',    LABEL_ADDR),    # Label address is an alphanumeric string followed by one colon
    (r'[A-Za-z][A-Za-z0-9_]*',      LABEL)          # Label is an alphanumeric string, not followed by one colon
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

def secondPass(instructions) :
    """
    Traversing the instruction dictionary, and replaceing the label with line numbers
    """
    # Mapping label to line number
    labelToLine = {}

    for lineNum in instructions :
        # If this is a LABEL_ADDR, it should be the first token
        first_token = instructions[lineNum][0]
        token_name = first_token[0]
        token_type = first_token[1]
        if token_type == LABEL_ADDR :
            # Remove the last character from label address, which is ":"
            labelName = token_name[:-1]
            labelToLine[labelName] = lineNum
        

if __name__ == "__main__" :
    exampleFile_1 = r"./examples/countTo10.alpl"
    exampleFile_2 = r"./examples/print2020.alpl"
    
    # Instruction dictionary
    # Key   : Line number
    # value : List of tokens
    instructions = {}

    file = open(exampleFile_2)
    #characters = file.read()
    lines = file.readlines()
    file.close()

    # Create instruction dictionary
    for idx, val in enumerate(lines) :
        instructions[idx] = lex(val)

    # Second pass - Replace label with line numbers
    secondPass(instructions)

    #tokens = lex(characters)
    #for token in tokens:
    #    print (token)
    print (instructions)