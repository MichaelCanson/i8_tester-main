'''
Copyright(c) 2023 Marquis Systems Inc.

'''
import sys
import os
import time
import csv
from datetime import  date
from binascii import hexlify 
from random import choice, choices, randrange
import logging
from pynput import keyboard
from i2c_controller import Controller
import i2c_defs


def main():
    if sys.argv[1] == '-bus':
        bus_addr = int(sys.argv[2])
        i2c_defs.BUS_ADDR = bus_addr
        print('bus_addr: {}'.format(bus_addr))
        controller = Controller()
    else:
        print('ERROR: missing args: bus address.')
        return 0
         
    if sys.argv[3] == '-n':
        print("number of trials to run: ", sys.argv[4])    
        trials = int(sys.argv[4])
    else:
        trials = 500000
    
    #------------ Test Log Configurations -----------------------
    duplicate_count = 0
    while os.path.exists(i2c_defs.TEST_LOG):
        duplicate_count += 1

        i2c_defs.LOG_TITLE = '{}({})'.format(date.today(),duplicate_count)
        i2c_defs.TEST_LOG = '{}/{}.txt'.format(i2c_defs.FILE_PATH,i2c_defs.LOG_TITLE)
    try:
        open(i2c_defs.TEST_LOG,'x')
    except:
        duplicate_count = int(i2c_defs.LOG_TITLE[-2]) + 1
        i2c_defs.LOG_TITLE = '{}({})'.format(date.today(),duplicate_count)
        i2c_defs.TEST_LOG = '{}/{}.txt'.format(i2c_defs.FILE_PATH,i2c_defs.LOG_TITLE)
        open(i2c_defs.TEST_LOG,'x')

    logging.basicConfig(filename= i2c_defs.TEST_LOG,filemode='a',level=logging.INFO,\
         format='%(asctime)s,%(message)s', datefmt='%D %H:%M:%S')
# ---------------------------------------------------------------
    
# ----------------- Test Configurations -------------------------
    test_type = i2c_defs.TESTS_TO_RUN[0][0]
    loop_count = trials
    while trials:
        print('Trial {} started'.format(trials))
        curr_count = loop_count - trials
        i8_count = 0
        for test in range(len(i2c_defs.TESTS_TO_RUN)):
                print('Test to run ix: {}'.format(test))

                #set pcf address
                num_i8_pairs = len(i2c_defs.I8_PAIR_ADDR) 
                if test < num_i8_pairs:
                    addr_ix = test
                
                else:    
                    addr_ix = (test % num_i8_pairs)
                controller.set_pcf_address(addr_ix)

                for i8_pair_ix in range(2):
                    i8_count += 1
                    print('i8_count: {}'.format(i8_count))
                    test_type = i2c_defs.TESTS_TO_RUN[test][i8_pair_ix]
                    logging.info('---,---,TEST #{} Trial:{} '
                    .format(test_type,curr_count))
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
                                    
                                logging.info('{0:X}: input {1} ACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))

                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        

                        else:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 2))
                            for i in range(len(i2c_defs.I0_ADDR)):
                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.I0_ADDR[i]
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],10 + i))
                                
                                logging.info('{0:X}: input {1} ACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))

                                time.sleep(i2c_defs.ACTIVE_DELAY)

                    elif test_type == 1:
                       
                        if not i8_pair_ix:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 1))
                            for i in range(len(i2c_defs.I0_ADDR_1)):
                                
                                controller.word_reg[addr_ix][0] = i2c_defs.I0_ADDR_1[i]
                                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],i))
                                
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))

                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))

                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))

                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        else:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 2))
                            for i in range(len(i2c_defs.I0_ADDR_1)):
                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.I0_ADDR_1[i]
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],10 + i))
                                
                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR) - 1- i)))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                controller.i2c.write(bytearray(controller.word_reg[addr_ix]))

                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))

                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        
                    logging.info('---,---,END OF TEST #{} Trial: {}'
                        .format(test_type,curr_count))

                #Reset
                controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                controller.i2c.write(bytearray([controller.word_reg[addr_ix][0],\
                                        controller.word_reg[addr_ix][1]]))       
        trials -= 1
        #---------------------------------------------------------------

    csv_log = '{}/{}.csv'.format(i2c_defs.CSV_PATH,i2c_defs.LOG_TITLE)
    with open(i2c_defs.TEST_LOG,'r') as input_file:
        stripped = (line.strip() for line in input_file)
        lines = (line.split(",") for line in stripped if line)
        with open(csv_log, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(('Timestamp','iSTAR i8','Input Port'))
            writer.writerows(lines)
    print('test trials has been completed.')

if __name__ == '__main__':
    sys.exit(main())


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