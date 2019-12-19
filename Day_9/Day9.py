import operator as op
import logging
from itertools import permutations

class Intcode_computer():


    def __init__(self,program_name,program,required_memory=200):

        if len(program)>required_memory:
            print('More memory reqired')
            quit()
        self.program = program
        
        self.memory = [0 for i in range(required_memory)]
        self.memory[:len(self.program)] = self.program[:] # 

        self.program_name = program_name

        self.output_data = []
        logger.info(f"Program {self.program_name} loaded")
        self.suspend = False
        self.pointer = 0 
        self.complete = False
        self.relative = 0
        self.execution_count = 0
        self.execution_list = []

    def __repr__(self):
        return  (f' Program: {self.program_name}, pointer {self.pointer}')

    def reset(self):
        '''
        resets memory to original state
        '''
        self.memory = self.program[:]
        self.pointer = 0
        self.output_data = []
        logger.info("Computer running {self.program_name} reset")

        # instruction is n places long. Two least significant places are 
        # op code, remainder are the access modes 
    
    def run(self,i_o_mode):
        '''
        executes the program currently in memory
        '''
        self.i_o_mode = i_o_mode
        ### HELPERS
        def fetch_command():
            '''
            Parses each instruction onto an op-code and mode data if it exists
            '''
            # Mode data returned as an integer. Maybe better use a string 
            assert(self.pointer < len(self.memory)), "Command fetch out of range"
            command = self.memory[self.pointer]  # read instruction from current pointer

            if command < 100:  # if there are fewer than 3 digits
                op_code = command # instruction has no mode data
                i_modes = None
            else: 
                i_modes = command//100  # strip out two least significant digits
                op_code = command -  100*(i_modes) # strip out most significant digits

            self.pointer += 1  
            return op_code,i_modes  

        def fetch_operands(mode,op_count):

            '''fetches from the memory location of each of operands based on the
            mode for each one and returns to function as a list'''
            assert (self.pointer<len(self.memory)-1),"Operand fetch out of range - {self.pointer}"
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
                elif s=='2':
                    data_location = self.memory[self.pointer] + self.relative
                else:
                   data_location = self.memory[self.pointer] # position mode 
                res.append(data_location) 
                self.pointer += 1  # increment pointer for each operand read
            return res
        
        ### OPERATIONS
        # one for each operation the computer can execute    
       
        def add(mode): 
            '''
            Op code 01 - fetches two operands, multiples them together and stores in the location
            identified by third operand
            '''
            x,y,z=  fetch_operands(mode,3)
            a = self.memory[x]
            b = self.memory[y]
            self.memory[z] = a+b

            return True

        def multiply(mode):
            '''
            Op code 02 - fetches two operands, multiples them together and stores in the location
            identified by third operand
            '''
            x,y,z=  fetch_operands(mode,3)
            a = self.memory[x]
            b = self.memory[y]
            self.memory[z] = a*b
            return True

        def input_integer(mode):
            '''
            Opcode 03 Prompts user to enter integer and stores it at the address in the operand
            If no input is passed at runtime, requests user input'''
            if not self.i_o_mode:  
                no_integer_entered = True
                while no_integer_entered:
                    # print(no_integer_entered)
                    s = input("Please enter an integer : ")

                    try:
                        i = int(s)
                        no_integer_entered = False
                    except:
                        pass
            
            else:
                # TODO Fetch the next input from the input list until list exhausted
                try:
                    i = next(self.input_data)
                except StopIteration:
                    self.suspend = True
                    self.pointer -= 1 # decrement pointer so that input instruction is reexecuted
                    logger.debug('Amplifier {self.program_name} suspended', )
                    return
            operand = fetch_operands(mode,op_count = 1)   # fetch 1 operand
            self.memory[operand[0]]= i 
            logger.debug('User entered value %s. Written to location %s',int(i),self.memory[self.pointer])
            logger.debug(f'Pointer is {self.pointer}')
            no_integer_entered = False
            # if not self_i_o_mode: # increment pointer next instruction
            #     self.pointer += 1 # if in 

            return 1

        def output_memory_location(mode):
            '''
            Opcode 04 -outputs to stdout the data stored at the memory location in the operand
            '''
            # logger.debug(f'Output {self.memory[self.pointer]}')
            logger.debug(f'Pointer is {self.pointer}')
            operand = self.memory[fetch_operands(mode,1)[0]]
            
            if not self.i_o_mode:
                print(operand)
            self.output_data.append(operand)
            # assert (operand[0] == 0 ) , "Non-zero code output"

            # self.pointer += 1 # increment pointer to next instruction
            return 1 
            
        def jump_if_true(mode):
            '''
            Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets 
            the instruction pointer to the value from the second parameter. Otherwise, 
            it does nothing.
            '''
            x,y =  [self.memory[op] for op in fetch_operands(mode,2)]

            if x:
                self.pointer = y
            return

        def jump_if_false(mode):
            '''
            Opcode 6 is jump-if-false: if the first parameter is zero, it sets the 
            instruction pointer to the value from the second parameter. 
            Otherwise, it does nothing.

            '''
            x,y =  [self.memory[op] for op in fetch_operands(mode,2)]

            if not x:
                self.pointer = y
            return

        def less_than(mode):
            '''
            compares first two operands and puts a 1 in the mem location of third
            operand if first is less than second. otherwise a zero
            '''
            x,y,z=  fetch_operands(mode,3)
            a = self.memory[x]
            b = self.memory[y]
            self.memory[z] = int(a<b)
            # self.pointer += 1
            return

        def equals(mode):
            '''
            compares first two operands and puts a 1 in the mem location of third
            operand if first equal to second, otherwise a zero
            '''           
            x,y,z=  fetch_operands(mode,3)
            a = self.memory[x]
            b = self.memory[y]
            self.memory[z] = int(a==b)
            # self.pointer += 1
            return

        def adjust_relative(mode):
            x = self.memory[fetch_operands(mode, 1)[0]]
            self.relative += x
            # self.pointer += 1
            return


        # Dictionary to call the correct function
        EXECUTE =  {1:add,  # computer instruction set
                    2:multiply,
                    3:input_integer,
                    4:output_memory_location,
                    5:jump_if_true,
                    6:jump_if_false,
                    7:less_than,
                    8:equals,
                    9:adjust_relative}

        ####
        ## Code starts
        logger.info(" ")
        logger.info(f'running program {self.program_name} ')


        # initialize address pointer
        if self.i_o_mode:  # if data is present at input use that instead of input from keyboard
            self.input_data = (i for i in self.i_o_mode)
        else:
            self.input_data = None

        logger.debug(f'instruction pointer is {self.pointer}')

        # Fetch  first instruction
        op_code,modes = fetch_command()  
        #Main loop 
        while  not (op_code==99 or self.suspend) :   # end of program reached
            self.execution_count += 1
            try:   #  ensures that any memory reads or writes out of range are trapped

                logger.debug(f'Running function is "{op_code}";  modes are {modes} ')  
                logger.debug(f'instruction pointer is {self.pointer}')

                assert(1<=op_code<=9), f"Invalid instruction code - {op_code} at pointer {self.pointer} and exec {self.execution_count}"
                self.execution_list.append((self.pointer, op_code,modes))
                EXECUTE[op_code](modes) # Select method to perform instruction
                                        # and pass parameter modes
            except Exception as e:
                # logger.error('Addresses out of range at pointer %s', self.pointer)
                print(e)
                return 0   # if it fails return 0
            
            if not self.suspend:
                op_code,modes = fetch_command()
            if op_code == 99:
                self.complete = True
        return(self.output_data)        

    def resume(self, new_input_data):
        '''
        restarts code where it left off when it suspended after input data ran out
        '''
        self.suspend = False
        
        self.i_o_mode = new_input_data
        self.output_data = []
        return self.run(new_input_data)
        


class PROGS():

    DAY9TEST1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    DAY9TEST2 = [1102,34915192,34915192,7,4,7,99,0]
    DAY9TEST3 = [104,1125899906842624,99]

    with open('Day_9\input.txt','r') as f:
        DAY9_PROGRAM = [int(s) for s in f.read().strip().split(',')]

#####################################
# R
if __name__ == "__main__":

    ##############################################
    ## Logging Configuration
    FORMAT = '%(asctime)-15s %(funcName)s:%(message)s'
    logging.basicConfig(format=FORMAT,level = logging.DEBUG,filename='Day_7\\runlog.txt')
    logger = logging.getLogger(__name__)

    # test_data = [PROGS.DAY9TEST1,PROGS.DAY9TEST2,PROGS.DAY9TEST3]
    # results9 = {1: }

    # test1 = lambda x,y: assert (x.output_data==y) , "Test 1 failed"

    # for i,td in enumerate(test_data):

    #     computer = Intcode_computer('Test'+str(i),td,required_memory = 200)

    #     computer.run([])
    #     assert (x.output_data==y) , "Test 1 failed"
    BOOST = Intcode_computer('BOOST',PROGS.DAY9_PROGRAM, required_memory= 2048)
    BOOST.run([])
   






