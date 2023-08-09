'''
Copyright(c) 2023 Marquis Systems Inc.

'''
from datetime import date

DISABLE_i8 = 0xff

BUS_ADDR = 0x01
# I8_PAIR_ADDR =  [0x20,0x23,0x20,0x23] #PCF address with constant pcf value and LSB: R/W bit set to 1.
# I2C_BUS_EXP_PAIR = [(0x01,0x20), (0x01,0x23),\
#                     (0x02,0x21), (0x02,0x22)]
I2C_BUS_EXP_PAIR = [(0x02,0x22),(0x02,0x22),\
                    (0x02,0x22),(0x02,0x22)]
I8_PAIR_ADDR =  [0x21,0x22]
WORD_REG = [[0xff,0xff],[0xff,0xff],[0xff,0xff],[0xff,0xff]] 
ACTIVE_DELAY = 2
ACTIVE_DURATION = 2
SEQ = 0
RAND_PAIRS = 1

TEST0 = [0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f] #In sequence testing
# TEST1 = [0xbd,0xbd,0xbd,0xbd,0xbd,0xbd,0xbd,0xbd]
TEST1 = [0xfd,0xfd,0xfd,0xfd,0xfd,0xfd,0xfd,0xfd]
# TEST1 = [0x7e, 0xbd, 0xdb, 0xe7] #two inputs active within the same pcf  

# TESTS_TO_RUN =[(TEST1,TEST1),(TEST1,TEST1),\
#                (TEST1,TEST1),(TEST1,TEST1)]
TESTS_TO_RUN =[(TEST0,TEST0),(TEST0,TEST0),\
               (TEST0,TEST0),(TEST0,TEST0)]

FILE_PATH = '/home/kampr/i8_tester-main/i8_tester/logs'
CSV_PATH = '/home/kampr/i8_tester-main/i8_tester/logs/csv'
LOG_TITLE = '{}'.format(date.today())
TEST_LOG = '{}/{}.txt'.format(FILE_PATH,LOG_TITLE)
WINDOW_IMG = '/home/kampr/i8_tester-main/i8_tester/Marquis_New-Colors-100x72-at-300.png'