#!/usr/bin/env python

"""
ALPL_Interpreter - An Interpreterimplementation for the ALPL language, built for myInterpreter 
Code based on https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
"""
import sys

class Interpreter:
    def __init__(self, alpl_file):
        """
        Interpreter holds the current program counter,
        the call stack return line number, and the register file
        """
        # Init object data
        self.programCnt = 0
        self.call_stack = []
        self.regs = [0 for i in range(self.REG_FILE_SIZE)]
        
        # Parse input source file
        file = open(alpl_file)
        lines = file.readlines()
        file.close()

        # Lexer
        self.instructions = ALPL_Lexer.createInstructions(lines)
        
    def LET_CMD (self) :
        pass

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
        
    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)

            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(argument)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            elif instruction == "STORE_NAME":
                self.STORE_NAME(argument)
            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(argument)        
        
if __name__ == "__main__" :
    if len(sys.argv) != 3 :
        print ("ALPL_Interpreter syntax:\npython ALPL_Interpreter ALPL_file")
        sys.exit(1)
    alpl_file = sys.argv[2]
    
    # Create Interpreter object
    interObj = Interpreter(alpl_file)
    
    # Run interpreter
    interObj.run_code()
    
    
    