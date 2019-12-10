import operator as op
import logging
PROGRAM = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0]
# PROGRAM = [
# 1,0,0,3,\
# 1,1,2,3,\
# 1,3,4,3,\
# 1,5,0,3,\
# 2,1,6,19,\
# 1,9,19,23,\
# 1,6,23,27,\
# 1,10,27,31,
# 1,5,31,35,
# 2,6,35,39,
# 1,5,39,43,
# 1,5,43,47,
# 2,47,6,51,
# 1,51,5,55,
# 1,13,55,59,
# 2,9,59,63,
# 1,5,63,67,
# 2,67,9,71,
# 1,5,71,75,
# 2,10,75,79,
# 1,6,79,83,
# 1,13,83,87,
# 1,10,87,91,
# 1,91,5,95,
# 2,95,10,99,
# 2,9,99,103,
# 1,103,6,107,
# 1,107,10,111,
# 2,111,10,115,
# 1,115,6,119,
# 2,119,9,123,
# 1,123,6,127,
# 2,127,10,131,
# 1,131,6,135,
# 2,6,135,139,
# 1,139,5,143,
# 1,9,143,147,
# 1,13,147,151,
# 1,2,151,155,
# 1,10,155,0,
# 99,2,14,0,0]

TARGET_OUTPUT = 19690720

OPERATOR = {1:op.add,
            2:op.mul}

##############################################3
## Logging Configuration
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT,level = logging.INFO,filename='Day 2\\runlog.txt')
logger = logging.getLogger(__name__)



def Intcode_computer(noun,verb,program):
    memory = program.copy()
    memory[1]=noun # initialize noun
    memory[2]=verb # initialize verb
    # print(memory)
    logger.info(" ")
    logger.info(f'trying noun {noun } and verb {verb}')
    
    pointer = 0  # initialize address pointer
    logger.debug(f'instruction pointer is {pointer}')
    op_code = memory[pointer]  
    
    while  op_code!=99:   # end of program reached
        try:   #  ensures that any memory reads or writes out of range are trapped
            parameters = memory[pointer+1:pointer+4]
            operands = memory[parameters[0]],memory[parameters[1]]  # read the operands from memory
            memory[parameters[2]] = OPERATOR[op_code](*operands) # execute instruction and store in memory
            logger.debug('Instruction is %s;  Operands are %s; Result is %s; Addresses are %s;', OPERATOR[op_code].__name__,operands,memory[parameters[2]],parameters)
        except Exception as e:
            logger.error('Addresses out of range. %s,%s,%s', *parameters)
            return 0   # if it fails return 0
        pointer += 4   # advance instruction pointer
        op_code = memory[pointer] # read next instruction

    return(memory[0])        

for n in range(100): # cycle through all possible nouns
    answer_found=False
    for v in range(100): # cycle through all possible verbs
        res = Intcode_computer(n,v,PROGRAM)
        print(f'result is {res}')
        logging.info('Result is %s',res)
        if res == TARGET_OUTPUT:
            print(f'Answer found {100*n+v}')
            answer_found=True
            break
    if answer_found:
        break



# TEST = [1,9,10,3,2,3,11,0,99,30,40,50]

# print(Intcode_computer(12,2,TEST))



# test_data= [
#     [1,0,0,0,99,0,0] ,
#     [2,3,0,3,99,0,0],
#     [2,4,4,5,99,0,0],
#     [1,1,1,4,99,5,6,0,99,0,0]
# ],
# [ [2,0,0,0,99] , [2,3,0,6,99], [2,4,4,5,99,9801],[30,1,1,4,2,5,6,0,99]]