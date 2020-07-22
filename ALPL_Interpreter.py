#!/usr/bin/env python

"""
ALPL_Interpreter - An Interpreterimplementation for the ALPL language, built for myInterpreter 
Code based on https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
"""
import sys

import ALPL_Lexer
from ALPL_Lexer import RESERVED, INT , LABEL, REG, OP_ADD, OP_MULT

import ALPL_Parser

class Interpreter:
    # Class constans
    # Register file size
    REG_FILE_SIZE = 10

    def __init__(self, alpl_file):
        """
        Interpreter holds the current program counter,
        the call stack return line number, and the register file
        """
        # Init object data
        self.programLineNum = 0
        self.call_stack = []
        self.regs = [0 for i in range(self.REG_FILE_SIZE)]
        
        # Parse input source file
        file = open(alpl_file)
        lines = file.readlines()
        file.close()

        # Run Lexer on input lines
        self.instructions = ALPL_Lexer.createInstructions(lines)
        
        self.endOfLineNumber = len(self.instructions)

    def LET_CMD (self) :
        """
        Execute LET command
        """
        currLine = self.instructions[self.programLineNum]       

        # Send to parser the line without the OpCode, which is the first token
        parser = ALPL_Parser.parser(currLine[1:], self.regs)

        # Perform the register assignment
        self.regs = parser.assign()

        # Increase program counter
        self.programLineNum += 1

    def IF_CMD (self) :
        pass
        
    def JUMP_CMD (self) :
        pass
        
    def CALL_CMD (self) :
        pass
        
    def RETURN_CMD (self) :
        pass        
        
    def PRINT_CMD (self) :
        pass           
        
    def run_code(self):
        """
        Main running loop of ALPL script.
        Run each command, until reached end of line number
        """
        while self.programLineNum != self.endOfLineNumber :
            currLine = self.instructions[self.programLineNum]

            firstOpCode = currLine[0]
            opCodeType = firstOpCode[1]

            # Execute command in each new line
            if opCodeType == RESERVED :
                opCodeName = firstOpCode[0]
                if opCodeName == "LET" :
                    self.LET_CMD ()
                elif opCodeName == "IF" :
                    self.IF_CMD ()
                elif opCodeName == "JUMP" :
                    self.JUMP_CMD ()
                elif opCodeName == "CALL" :
                    self.CALL_CMD ()
                elif opCodeName == "RETURN" :
                    self.RETURN_CMD ()
                elif opCodeName == "PRINT" :
                    self.PRINT_CMD ()

            # Label adderss lines should be skipped
            elif oCodeType == LABEL_ADDR :
                self.programLineNum += 1
                continue       
    def print_inst (self) :
        """Pretty print the instructions"""
        print ("Parsed ALPL code :")
        import pprint 
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.instructions)

        print ("\nRegister file :")
        for i in range(self.REG_FILE_SIZE) :
            print (str(i) + ") " + str(self.regs[i]))


if __name__ == "__main__" :
    #if len(sys.argv) != 2 :
    #    print ("ALPL_Interpreter syntax:\n.\\ALPL_Interpreter ALPL_file")
    #    sys.exit(1)
    #alpl_file = sys.argv[1]
    
    # Debug
    alpl_file = r"./examples/simpleExpr.alpl"
    
    # Create Interpreter object
    interObj = Interpreter(alpl_file)
    
    # Run interpreter
    interObj.run_code()
    interObj.print_inst()

    
    
    