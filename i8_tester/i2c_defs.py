'''
Copyright(c) 2023 Marquis Systems Inc.

'''
from datetime import date

DISABLE_i8 = 0xff

BUS_ADDR = 0x01
I2C_BUS_EXP_PAIR = [(0x01,0x20), (0x01,0x21),\
                    (0x00,0x22), (0x00,0x23)]

I8_PAIR_ADDR =  [0x21,0x22]
WORD_REG = [[0xff,0xff],[0xff,0xff],
            [0xff,0xff],[0xff,0xff]]
NUM_OF_I8_PER_PCF = 2
ACTIVE_DELAY = 5
ACTIVE_DURATION = 8

# Tests
#TEST0 = [0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f] #In sequence testing
#TEST1 = [0x7e, 0xbd, 0xdb, 0xe7] #two inputs active within the same pcf  
#TEST2 = [0x3c, 0xc3] # 4 inputs active within the same pcf
#TEST3 = [0x7e, 0x7e, 0x7e, 0x7e] # 2 inputs triggered for each pcf
TEST1 = 0x7e 
TEST3 = 0x3c

TESTS_TO_RUN = [(TEST1,TEST1),(TEST1,TEST1), (TEST3,TEST3),(TEST3,TEST3)
                


]


FILE_PATH = '/home/ks/i8_tester-main/i8_tester/logs'
CSV_PATH = '/home/ks/i8_tester-main/i8_tester/logs/csv'
LOG_TITLE = '{}'.format(date.today())
TEST_LOG = '{}/{}.txt'.format(FILE_PATH,LOG_TITLE)
WINDOW_IMG = '/home/ks/i8_tester-main/i8_tester/Marquis_New-Colors-100x72-at-300.png'