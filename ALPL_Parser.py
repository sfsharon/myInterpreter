#!/usr/bin/env python

"""
ALPL_Parser - Parse the token list from the lexer

"""
import ALPL_Lexer
from ALPL_Lexer import RESERVED, INT , LABEL, REG, OP_ADD, OP_MULT

class parser(object) :
    def __init__ (self, tokens) :
        self.tokens = tokens
        self.tokenPos = 0
        
    def consumeToken(self, token_type) :
        if self.tokens[self.tokenPos][1] == token_type : # Compare token type
            self.tokenPos += 1
        else :
            raise Exception('Invalid Syntax')
            
    def factor(self) :
        token = self.tokens[self.tokenPos]
        self.consumeToken(INT)
        return int(token[0]) # Return Token value

    def expr(self) :
        result = self.factor()
        
        if self.tokens[self.tokenPos][1] in (OP_ADD, OP_MULT) :
            token = self.tokens[self.tokenPos]
            if token[1] == OP_MULT :
                self.consumeToken(OP_MULT)
                result = result * self.factor()
            elif token[1] == OP_ADD :
                self.consumeToken(OP_ADD)
                result = result + self.factor()
        return result

if __name__ == "__main__" :
    exampleFile_1 = r"./examples/simpleExpr.alpl"
    
    file = open(exampleFile_1)
    characters = file.read()
    file.close()
    tokens = ALPL_Lexer.lex(characters)
    myParser = parser(tokens)
    res = myParser.expr()
    print (res)



