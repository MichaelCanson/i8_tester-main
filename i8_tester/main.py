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
    # if sys.argv[1] == '-bus':
    #     bus_addr_ix = int(sys.argv[2])
    #     i2c_defs.BUS_ADDR = bus_addr_ix
    #     print('bus_addr_ix: {}'.format(bus_addr_ix))
    #     controller = Controller()
    # else:
    #     print('ERROR: missing args: bus address.')
    #     return 0
         
    if sys.argv[1] == '-n':
        print("number of trials to run: ", sys.argv[2])    
        trials = int(sys.argv[2])
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
    controller = Controller()
    while trials:
        print('Trial {} started'.format(trials))
        curr_count = loop_count - trials
        
        for test_ix in range(len(i2c_defs.TESTS_TO_RUN)):
                print('Test to run ix: {}'.format(test_ix))

                bus_addr_ix = i2c_defs.I2C_BUS_EXP_PAIR[test_ix][0]
                controller.set_i2c_bus(bus_addr_ix)

                #set pcf address
                # pcf_addr = i2c_defs.I2C_BUS_EXP_PAIR[test_ix][1]
                controller.set_pcf_address(test_ix,1)


                for i8_ix in range(2):
                    controller.run_test(test_type,test_ix,i8_ix,curr_count)

                #Reset
                controller.reset_test(test_ix)      
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
    print('test_ix trials has been completed.')

if __name__ == '__main__':
    sys.exit(main())
