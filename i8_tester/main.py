'''
Copyright(c) 2023 Marquis Systems Inc.

'''
import cv2
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


def main():
         
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
    loop_count = trials
    controller = Controller()

    while trials:
        curr_count = loop_count - trials                
        print('{} of {} Trials started'.format(curr_count,trials))
        logging.info('---,---,TEST Trial:{} '
                    .format(curr_count))
        controller.activate_inputs()

        time.sleep(i2c_defs.ACTIVE_DURATION)

        controller.deactivate_inputs()

        time.sleep(i2c_defs.ACTIVE_DELAY)

        logging.info('---,---,End of TEST Trial:{} '
                    .format(curr_count))
        
        trials -= 1
    logging.info('---,---,End of TEST Trial:{} '
                    .format(curr_count))
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
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main())
