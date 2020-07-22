#!/usr/bin/env python

"""
ALPL_Parser - Parse the token list from the lexer
Based on : https://ruslanspivak.com/lsbasi-part4/
"""
import re

import ALPL_Lexer
from ALPL_Lexer import RESERVED, INT , LABEL, REG, OP_ADD, OP_MULT

class parser(object) :
    ## Class constans
    ## Register file size
    #REG_FILE_SIZE = 10

    def __init__ (self, tokens, regs) :
        self.tokens = tokens
        self.tokenPos = 0
        
        # Register file
        self.regs = regs

    def consumeToken (self, tokenName) :

        if self.tokens[self.tokenPos][0] == tokenName:
            # Move to next token
            self.tokenPos += 1
        else:
            raise Exception('Invalid Syntax')
            
    def factor(self) :
        """
        Grammar rule 
        ===================
        factor : INT | REG
        Explanation : factor is either an integer of a register
        """
        token = self.tokens[self.tokenPos]
        rVal = 0

        if token[1] == INT :
            rVal = int(token[0]) 
        elif token[1] == REG :
            regex = re.compile(r'R([0-9])')
            match = regex.match(token[0])
            regIdx = int(match.group(1))
            rVal =  self.regs[regIdx]
        else :
            raise Exception('Invalid Syntax')

        # Move to next token
        self.tokenPos += 1
        # Return Token value
        return rVal

    def register(self) :
        """
        Grammar rule 
        ===================
        register : R[0-9]
        Explanation : Register is a string that begins with 'R', and a single digit from 0 to 9
        """
        token = self.tokens[self.tokenPos]

        if token[1] == REG :
            regex = re.compile(r'R([0-9])')
            match = regex.match(token[0])
            regIdx = int(match.group(1))
            #rVal =  self.regs[regIdx]
        else :
            raise Exception('Invalid Syntax')

        # Move to next token
        self.tokenPos += 1
        # Return register index
        return regIdx

    def expr(self) :
        """
        Grammar rule 
        =================== 
        expr : factor ((OP_MULT | OP_ADD) factor)?

        Explanation : expr is build from one factor, and none or one 
                      of (OP_MULT | OP_ADD) factor
        """
        result = self.factor()
        
        if self.tokens[self.tokenPos][1] in (OP_ADD, OP_MULT) :
            token = self.tokens[self.tokenPos]
            if token[1] == OP_MULT :                
                self.tokenPos += 1      # Move to next token
                result = result * self.factor()
            elif token[1] == OP_ADD :
                self.tokenPos += 1      # Move to next token
                result = result + self.factor()

        # Return result value
        return result

    def assign(self) :
        """
        Grammar rule 
        =================== 
        assign : R[0-9] := expr
        """
        # Get register index
        regIdx = self.register()

        # Consume the assignment operator
        self.consumeToken (':=')

        # Calculate assignment expression value
        exprVal = self.expr()

        # Perform the assignment
        self.regs[regIdx] = exprVal

        return self.regs


if __name__ == "__main__" :
    exampleFile_1 = r"./examples/countTo10.alpl"
    exampleFile_2 = r"./examples/print2020.alpl"
    
    file = open(exampleFile_2)
    lines = file.readlines()
    file.close()

    # Lexer
    instructions = ALPL_Lexer.createInstructions(lines)

    # Interpreter

    # Parser
    myParser = parser(tokens)
    res = myParser.expr()
    print (res)



