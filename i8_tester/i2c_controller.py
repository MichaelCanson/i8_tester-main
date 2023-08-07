'''
Copyright(c) 2023 Marquis Systems Inc.

'''
import time
import mraa 
import random
import i2c_defs
import logging
class Controller():

    def __init__(self):
        
        self.i2c = 0
        self.current_addr = 0
        
        self.curr_pin = 0xff
        self.word_reg = i2c_defs.WORD_REG
        self.close_delay = 0
        self.open_duration = 0


    def set_pcf_address(self, bus_addr_ix, ix):
        print('bus_addr_ix: {}'.format(bus_addr_ix))
        print('test_ix: {}'.format(ix))

        self.current_addr = i2c_defs.I2C_BUS_EXP_PAIR[bus_addr_ix][ix]
        print('current PCF Address: {}'.format(hex(self.current_addr)))
        res = self.i2c.address(self.current_addr)
        return self.current_addr
        # if not res:
        #     return self.current_addr
        # else:
        #     print('ERROR: failed to set pcf addr!')
        #     return 0

    def set_i2c_bus(self,bus):
        self.i2c = mraa.I2c(bus, True)
        print('I2C_Controller: BUS_ADDR: {0:x}'.format(bus))

    def run_test(self, test_type, test_ix, i8_ix, trial_count):
        
        if test_type == i2c_defs.TEST0:
            logging.info('---,---,TEST #0 Trial:{} '
                    .format(trial_count))
            if not i8_ix:
                print('\n---- i8.{} Test ----'.format(test_ix + 1))
                for i in range(len(i2c_defs.TEST0)):
                    self.word_reg[test_ix][0] = i2c_defs.TEST0[i]
                    self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
                    self.i2c.write(bytearray(self.word_reg[test_ix]))
                    print('i8.{} Output: {} enabled'
                        .format((test_ix * 2) + i8_ix + 1,i))
                        
                    logging.info('i8.{}: input {} ACTIVE,'
                                    .format((test_ix * 2) + i8_ix + 1, i))
                    
                    time.sleep(i2c_defs.ACTIVE_DURATION)

                    self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
                    self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
                    self.i2c.write(bytearray(self.word_reg[test_ix]))
                    logging.info('i8.{}: input {} INACTIVE,'
                                    .format((test_ix * 2) + i8_ix + 1, i))

                    time.sleep(i2c_defs.ACTIVE_DELAY)
            

            else:
                print('\n---- i8.{} Test ----'.format(test_ix + 2))
                for i in range(len(i2c_defs.TEST0)):
                    self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
                    self.word_reg[test_ix][1] = i2c_defs.TEST0[i]
                    self.i2c.write(bytearray(self.word_reg[test_ix]))
                    print('i8.{} Output: {} enabled'
                        .format((test_ix * 2) + i8_ix + 1,10 + i))
                    
                    logging.info('i8.{}: input {} ACTIVE,'
                                    .format((test_ix * 2) + i8_ix + 1, i))
                    
                    time.sleep(i2c_defs.ACTIVE_DURATION)

                    self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
                    self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
                    self.i2c.write(bytearray(self.word_reg[test_ix]))
                    logging.info('i8.{}: input {} INACTIVE,'
                                    .format((test_ix * 2) + i8_ix + 1, i))

                    time.sleep(i2c_defs.ACTIVE_DELAY)

        elif test_type == i2c_defs.TEST1:
            logging.info('---,---,TEST #1 Trial:{} '
                    .format(trial_count))
            if not i8_ix:
                print('\n---- i8.{} Test ----'.format(test_ix + 1))
                for i in range(len(i2c_defs.TEST1)):
                    
                    self.word_reg[test_ix][0] = i2c_defs.TEST1[i]
                    self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
                    self.i2c.write(bytearray(self.word_reg[test_ix]))

                    print('i8.{} Output: {} enabled'
                        .format((test_ix * 2) + i8_ix + 1,i + 1))
                    print('i8.{} Output: {} enabled'
                        .format((test_ix * 2) + i8_ix + 1,(len(i2c_defs.TEST1) + 1 + i)))

                    logging.info('i8.{}: input {} ACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1, i + 1))
                    logging.info('i8.{}: input {} ACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1,(len(i2c_defs.TEST1) + 1 + i)))
                    
                    time.sleep(i2c_defs.ACTIVE_DURATION)

                    self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
                    self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
                    self.i2c.write(bytearray(self.word_reg[test_ix]))

                    logging.info('i8.{}: input {} INACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1,i + 1))
                    logging.info('i8.{}: input {} INACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1, (len(i2c_defs.TEST1) + 1 + i)))

                    time.sleep(i2c_defs.ACTIVE_DELAY)
            else:
                print('\n---- i8.{} Test ----'.format(test_ix + 2))
                for i in range(len(i2c_defs.TEST1)):
                    self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
                    self.word_reg[test_ix][1] = i2c_defs.TEST1[i]
                    self.i2c.write(bytearray(self.word_reg[test_ix]))

                    
                    print('i8.{} Output: {} enabled'
                        .format((test_ix * 2) + i8_ix + 1,i + 1))
                    print('i8.{} Output: {} enabled'
                        .format((test_ix * 2) + i8_ix + 1,(len(i2c_defs.TEST1) + 1 + i)))

                    
                    logging.info('i8.{}: input {} ACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1, i + 1))
                    logging.info('i8.{}: input {} ACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1,(len(i2c_defs.TEST1) + 1 + i)))
                    
                    time.sleep(i2c_defs.ACTIVE_DURATION)

                    self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
                    self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
                    self.i2c.write(bytearray(self.word_reg[test_ix]))

                    logging.info('i8.{}: input {} INACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1, i + 1))
                    logging.info('i8.{}: input {} INACTIVE,'
                        .format((test_ix * 2) + i8_ix + 1, (len(i2c_defs.TEST1) + 1 + i)))

                    time.sleep(i2c_defs.ACTIVE_DELAY)
            
    def reset_test(self,test_ix):
        self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
        self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
        self.i2c.write(bytearray([self.word_reg[test_ix][0],\
        self.word_reg[test_ix][1]])) 

    def set_open_delay(self,sec):
        self.delay = sec


    def set_open_dur(self, sec):
        self.open_duration = sec
