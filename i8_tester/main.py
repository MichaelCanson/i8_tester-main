'''
Copyright(c) 2023 Marquis Systems Inc.

'''
import sys
import time
from i2c_controller import Controller
import i2c_defs

from binascii import hexlify 
from random import choice, choices, randrange



def main():
    controller = Controller()
         
    if sys.argv[1] == '-n':
        print("number of trials to run: ", sys.argv[2])    
        trials = int(sys.argv[2])
    
    test_type = i2c_defs.TESTS_TO_RUN[0][0]        
# ---------------------------------------------------------------
    while trials:
        print('Trial {} started'.format(trials))
        for test in range(len(i2c_defs.TESTS_TO_RUN)):
                print('Test to run ix: {}'.format(test))
                # for addr_ix in range(len(i2c_defs.I8_PAIR_ADDR)):
                #     controller.set_pcf_address(addr_ix)
                if test < 4:
                    addr_ix = test
                    print('addr_ix: {}'.format(addr_ix))
                else:    
                    addr_ix = (test % 4)
                    print('addr_ix1: {}'.format(addr_ix))
                controller.set_pcf_address(addr_ix)
                for i8_pair_ix in range(2):
                    test_type = i2c_defs.TESTS_TO_RUN[test][i8_pair_ix]

                    '''
                    Verify which i8 is to be triggered within the ones
                    configured in current pcf address
                    '''
                    if test_type == 0:
                        if not i8_pair_ix:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 1))
                            for i in range(len(i2c_defs.I0_ADDR)):
                                controller.word_reg[addr_ix][0] = i2c_defs.I0_ADDR[i]
                                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],i))
                            
                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        else:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 2))
                            for i in range(len(i2c_defs.I0_ADDR)):
                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.I0_ADDR[i]
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],10 + i))
                                
                                time.sleep(i2c_defs.ACTIVE_DELAY)

                    elif test_type == 1:
                        print('test type 1 selected successfuly')
                        time.sleep(1)
                #     i8_addr_1 = (choice(i2c_defs.I8_PAIR_ADDR), randrange(1))
                #     i8_addr_2 = (choice(i2c_defs.I8_PAIR_ADDR), randrange(1))
                #     out_addr_1 = choice(i2c_defs.I0_ADDR)
                #     out_addr_2 = choice(i2c_defs.I0_ADDR)

                #     #eliminate the same pins on the same board from being assigned
                #     while out_addr_1 == out_addr_2:
                #         out_addr_2 = choice(i2c_defs.I0_ADDR)

                #     rand_i8_pair = [(i8_addr_1,out_addr_1),(i8_addr_2,out_addr_2)]

                #     #set rand order of which of the pair is to be enabled first. 
                #     rand_sequence = choices(rand_i8_pair)
                #     while rand_sequence[0] == rand_sequence[1]:
                #         rand_sequence = choices(rand_i8_pair)
                    
                # #     #TODO ^^ eliminates i8 boards to be selected that are paired in one pcf.
                # #     #set delay time
                #     active_delay_1 = 0
                #     active_dur_1 = randrange(3,8)

                #     active_delay_2 = randrange(1,3)
                #     active_dur_2 = randrange(3,8)

                #Reset
                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                controller.i2c.write(bytearray([controller.word_reg[addr_ix][0],\
                                        controller.word_reg[addr_ix][1]]))
                

        trials -= 1
    print('test trials has been completed.')
#---------------------------------------------------------------

if __name__ == '__main__':
    sys.exit(main())