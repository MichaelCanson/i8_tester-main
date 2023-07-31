'''
Copyright(c) 2023 Marquis Systems Inc.

'''
from datetime import date

DISABLE_i8 = 0xff

BUS_ADDR = 0x02
I8_PAIR_ADDR =  [0x20,0x21,0x22,0x23] #PCF address with constant pcf value and LSB: R/W bit set to 1.
WORD_REG = [[0xff,0xff],[0xff,0xff],[0xff,0xff],[0xff,0xff]] 
I0_ADDR = [0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f]

ACTIVE_DELAY = 1
ACTIVE_DURATION = 2
SEQ = 0
RAND_PAIRS = 1
TESTS_TO_RUN =[(0,0),(0,0),(0,0),(0,0)]

FILE_PATH = '/home/kampr/i8_tester-main/i8_tester/logs'
CSV_PATH = '/home/kampr/i8_tester-main/i8_tester/logs/csv'
LOG_TITLE = '{}'.format(date.today())
TEST_LOG = '{}/{}.txt'.format(FILE_PATH,LOG_TITLE)