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
from i2c_controller import Controller
import i2c_defs

I_IDLE_STATE = 0
I_ON_STATE = 1
I_ON_TIME_STATE = 2
I_OFF_STATE = 3
I_OFF_TIME_STATE = 4

app_state = I_IDLE_STATE

def run_xxx():

    
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
                Controller.set_pcf_address(addr_ix)

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
                                Controller.word_reg[addr_ix][0] = i2c_defs.I0_ADDR[i]
                                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],i))
                                    
                                logging.info('{0:X}: input {1} ACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))

                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        

                        else:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 2))
                            for i in range(len(i2c_defs.I0_ADDR)):
                                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                Controller.word_reg[addr_ix][1] = i2c_defs.I0_ADDR[i]
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],10 + i))
                                
                                logging.info('{0:X}: input {1} ACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                             .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))

                                time.sleep(i2c_defs.ACTIVE_DELAY)

                    elif test_type == 1:
                       
                        if not i8_pair_ix:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 1))
                            for i in range(len(i2c_defs.I0_ADDR_1)):
                                
                                Controller.word_reg[addr_ix][0] = i2c_defs.I0_ADDR_1[i]
                                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],i))
                                
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))

                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))

                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))

                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        else:
                            print('\n---- i8.{} Test ----'.format(addr_ix + 2))
                            for i in range(len(i2c_defs.I0_ADDR_1)):
                                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                Controller.word_reg[addr_ix][1] = i2c_defs.I0_ADDR_1[i]
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))
                                print('PCF ADDR: 0x{0:X} Output: {1} enabled'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],10 + i))
                                
                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} ACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR) - 1- i)))
                                
                                time.sleep(i2c_defs.ACTIVE_DURATION)

                                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                                Controller.i2c.write(bytearray(Controller.word_reg[addr_ix]))

                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix], i))
                                logging.info('{0:X}: input {1} INACTIVE,'
                                    .format(i2c_defs.I8_PAIR_ADDR[addr_ix],(len(i2c_defs.I0_ADDR)- 1 - i)))

                                time.sleep(i2c_defs.ACTIVE_DELAY)
                        
                    logging.info('---,---,END OF TEST #{} Trial: {}'
                        .format(test_type,curr_count))

                #Reset
                Controller.word_reg[addr_ix][0] = i2c_defs.DISABLE_i8
                Controller.word_reg[addr_ix][1] = i2c_defs.DISABLE_i8
                Controller.i2c.write(bytearray([Controller.word_reg[addr_ix][0],\
                                        Controller.word_reg[addr_ix][1]]))       
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


def turn_off_inputs ():
    pass
    # loop through bus-pcf-i8s and turn off inputs previously turned on 



def keep_inputs_on(duration):
    time.sleep(duration)

def turn_on_inputs(): 

    # loop through the bus-pcf-i8 and turn on inputs asked by test 
    for bus in range (2):
        Controller.set_i2c_bus(bus)
        for pcf in range (2):
            Controller = Controller.set_pcf_address(pcf)
            index = bus * pcf + pcf 
            Controller.word_reg[addr_ix][0] = i2c_defs.TEST_TO_RUN[index][0]
            Controller.word_reg[addr_ix][1] = i2c_defs.TEST_TO_RUN[index][1]
            Controller.i2c.write(bytearray([Controller.word_reg[addr_ix][0],\
                                        Controller.word_reg[addr_ix][1]]))       
 


def keep_inputs_off(duration):
    time.sleep(duration)

def main():
        
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

    loop_count = trials
    while trials:

        print('Trial {} started'.format(trials))
        curr_count = loop_count - trials
 
        app_state = I_IDLE_STATE

        # pass the table that contains which inputs to turn on across all I8s 
        app_state = I_ON_STATE
        turn_on_inputs( i2c_defs.TEST0)
        
        app_state = I_ON_TIME_STATE
        keep_inputs_on (delay_time_table)

        app_state = I_OFF_STATE
        turn_off_inputs (i2c_defs.TEST0)

        app_state = I_OFF_TIME_STATE
        keep_inputs_off (delay_time_table)


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


     