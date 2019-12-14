import operator as op
import logging

class Intcode_computer():


    def __init__(self,program_name,program):

        self.program = program
        self.memory = self.program[:] # 
        self.program_name = program_name
        logger.info(f"Program {self.program_name} loaded")
        self.pointer = 0 
        self.curr_instruction = self.memory[0]

    def __repr__(self):
        return  (f' Program: {self.program_name}, pointer {self.pointer}, instruction {self.curr_instruction}')

    def reset(self):
        '''
        resets memory to original state
        '''
        self.memory = self.program[:]
        logger.info("Computer running {self.program_name} reset")





        # instruction is n places long. Two least significant places are 
        # op code, remainder are the access modes 
    
    def run(self):
        '''
        executes the program currently in memory
        '''
        ### HELPERS
        def fetch_command():
            '''
            Parses each instruction onto an op-code and mode data if it exists
            '''
            # Mode data returned as an integer. Maybe better use a string 

            command = self.memory[self.pointer]  # read instruction from current pointer

            if command<100:  # if there are fewer than 3 digits
                op_code = command # instruction has no mode data

                i_modes = None
            else: 
                i_modes = command//100  # strip out two least significant digits
                op_code = command -  100*(i_modes) # strip out most significant digits

            self.pointer += 1  
            return op_code,i_modes  

        def fetch_operands(mode,op_count):

            '''fetches from memory each of operands based on the
            mode for each one and returns to function as a list'''
            if mode:
                s_mode = str(mode)[-1::-1] #convert to string and reverse
                s_mode = s_mode + (op_count - len(s_mode)) * '0' # pad with zeroes to required number
           
            else:
                s_mode = '0' * op_count   # every operand is postion mode  

            res = []
            # if no mode specified, mode is 0, two operands
            for s in s_mode:   # s_mode must have one entry for each operand
                if s=='1':
                    data_location = self.pointer  # direct mode
                else:
                   data_location = self.memory[self.pointer] # position mode 
                res.append(self.memory[data_location]) 
                self.pointer += 1   
            return res
       

             
        
            
        ### OPERATIONS
        # one for each operation the computer can execute    
       
        def input_integer(mode=None):
            '''
            Prompts user to enter integer
            '''
            no_integer_entered = True
            while no_integer_entered:
                # print(no_integer_entered)
                i = input("Please enter an integer : ")
                
                try:
                    self.memory[self.memory[self.pointer]]=int(i)
                    logger.debug('User entered value %s. Written to location %s',int(i),self.memory[self.pointer])
                    logger.debug(f'Pointer is {self.pointer}')
                    no_integer_entered = False
                except Exception:
                    pass
                finally:
                    self.pointer += 1  # increment pointer next instruction

            return 1

        def output_memory_location(mode):
            '''
            outputs the data to the memory location stored at the pointer
            always functions in postion mode
            '''
            logger.debug(f'Output {self.memory[self.memory[self.pointer]]}')
            logger.debug(f'Pointer is {self.pointer}')
            operand = fetch_operands(0,1)
            print(operand[0])            

            # self.pointer += 1 # increment pointer to next instruction
            return 1 

        def add(mode): 
            '''
            fetches two operands, multiples them together and stores in the location
            identified by third operand
            '''
            x,y = fetch_operands(mode,2)   # 
            self.memory[self.memory[self.pointer]] = x+y

            self.pointer += 1

            return True

        def multiply(mode):
            '''
            fetches two operands, multiples them together and stores in the location
            identified by third operand
            '''
            x,y = fetch_operands(mode,2)
            self.memory[self.memory[self.pointer]] = x*y
            self.pointer += 1
            return True

   
        # Dictionary to call the correct function
        EXECUTE =  {1:add,  # computer instruction set
                    2:multiply,
                    3:input_integer,
                    4:output_memory_location,
                    5:jump_if_true,
                    6:jump_if_false,
                    7:less_than,
                    8:equals}

    # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.

        ####
        ## Code starts
        logger.info(" ")
        logger.info(f'running program {self.program_name} ')


        # initialize address pointer
 
        logger.debug(f'instruction pointer is {self.pointer}')
        # fetch first instruction
        op_code,modes = fetch_command()  
        #Main loop 
        while  op_code!=99:   # end of program reached
            try:   #  ensures that any memory reads or writes out of range are trapped

                logger.debug(f'Function is "{EXECUTE[op_code].__name__}";  modes are {modes} ')  
                logger.debug(f'instruction pointer is {self.pointer}')
                EXECUTE[op_code](modes) # Select method to perform instruction
                                        # and pass parameter modes
            except Exception as e:
                # logger.error('Addresses out of range at pointer %s', self.pointer)
                print(e)
                return 0   # if it fails return 0
            
            op_code,modes = fetch_command()

        return(self.memory[0])        



class PROGS():
    DIAGNOSTIC = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,88,66,225,101,8,125,224,101,-88,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,87,23,225,1102,17,10,224,101,-170,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,9,65,225,1101,57,74,225,1101,66,73,225,1101,22,37,224,101,-59,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,79,64,225,1001,130,82,224,101,-113,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1102,80,17,225,1101,32,31,225,1,65,40,224,1001,224,-32,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,2,99,69,224,1001,224,-4503,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1002,14,92,224,1001,224,-6072,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,102,33,74,224,1001,224,-2409,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,344,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,449,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,479,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,524,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,554,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,569,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,644,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
    TEST = [3,0,4,0,99]
    SIMPLE_ADD = [3,0,3,2,1,0,2,0,4,0,99]
    SIMPLE_MULTIPLY = [1002,4,3,4,33]


if __name__ == "__main__":

    
    ##############################################
    ## Logging Configuration
    FORMAT = '%(asctime)-15s %(funcName)s:%(message)s'
    logging.basicConfig(format=FORMAT,level = logging.DEBUG,filename='Day_5\\runlog.txt')
    logger = logging.getLogger(__name__)


    diagnostic_test = Intcode_computer("DIAGNOSTICS",PROGS.DIAGNOSTIC)
    diagnostic_test.run()
    
    # test_io = Intcode_computer("IO Test",PROGS.TEST)
    # test_io.run()

    # simple_add = Intcode_computer("Simple Add",PROGS.SIMPLE_ADD)
    # simple_add.run()
    # simple_multiply = Intcode_computer("Simple MULTIPLY",PROGS.SIMPLE_MULTIPLY)
    # simple_multiply.run()
    # print (simple_multiply.memory)
    # print(diagnostic_test)








