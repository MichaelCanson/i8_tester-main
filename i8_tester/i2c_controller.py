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
        self.activated_inp = []


    def set_pcf_address(self, address):
       
        self.current_addr = address
        res = self.i2c.address(self.current_addr)
        print('current PCF Address: {}'.format(hex(self.current_addr)))
        print('set_pcf_address resp: {}'.format(res))
        return self.current_addr


    def set_i2c_bus(self,bus):
        self.i2c = mraa.I2c(bus, True)
        print('I2C_Controller: BUS_ADDR: {0:x}'.format(bus))

       
    def activate_inputs(self):
        for test_ix in range(len(i2c_defs.I2C_BUS_EXP_PAIR)):
            self.set_i2c_bus(i2c_defs.I2C_BUS_EXP_PAIR[test_ix][0])
            time.sleep(0.005)
            self.set_pcf_address(i2c_defs.I2C_BUS_EXP_PAIR[test_ix][1])
            time.sleep(0.005)

            
            self.word_reg[test_ix][0] = i2c_defs.TESTS_TO_RUN[test_ix][0]
            self.word_reg[test_ix][1] = i2c_defs.TESTS_TO_RUN[test_ix][1]
            self.i2c.write(bytearray(self.word_reg[test_ix]))
            time.sleep(0.005)
            self.log_inputs(test_ix, 0,\
                                i2c_defs.TESTS_TO_RUN[test_ix][0], "ACTIVE")
            self.log_inputs(test_ix, 1,\
                                i2c_defs.TESTS_TO_RUN[test_ix][1], "ACTIVE")


    def deactivate_inputs(self):
        for test_ix in range(len(i2c_defs.I2C_BUS_EXP_PAIR)):
            self.set_i2c_bus(i2c_defs.I2C_BUS_EXP_PAIR[test_ix][0])
            time.sleep(0.005)
            self.set_pcf_address(i2c_defs.I2C_BUS_EXP_PAIR[test_ix][1])
            time.sleep(0.005)

            
            self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
            self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
            self.i2c.write(bytearray(self.word_reg[test_ix]))
            time.sleep(0.005)
            self.log_inputs(test_ix, 0,\
                            i2c_defs.TESTS_TO_RUN[test_ix][0], "INACTIVE")
            self.log_inputs(test_ix, 1,\
                            i2c_defs.TESTS_TO_RUN[test_ix][1], "INACTIVE")


    def reset_test(self,test_ix):
        self.word_reg[test_ix][0] = i2c_defs.DISABLE_i8
        self.word_reg[test_ix][1] = i2c_defs.DISABLE_i8
        self.i2c.write(bytearray([self.word_reg[test_ix][0],\
        self.word_reg[test_ix][1]])) 

    def set_open_delay(self,sec):
        self.delay = sec


    def set_open_dur(self, sec):
        self.open_duration = sec

    
    def log_inputs(self,test_ix, i8_ix, test_val, state):
        hex_val = test_val
        # print('State: {}'.format(state))
        # print(hex_val)
        int_val = int(str(hex_val), base=10)
        bin_val = str(bin(int_val))[2:].zfill(8)
        print('bin_val: {}'.format(bin_val))
        
        if state == 'ACTIVE':
            for inp_ix in range(len(bin_val)):
                
                if bin_val[inp_ix] == '0':
                    self.activated_inp.append(inp_ix)
                    logging.info('i8.{}: input {} ACTIVE,'
                                        .format((test_ix * 2) + i8_ix + 1, inp_ix + 1))
        if state == 'INACTIVE':
            for inp_ix in range(len(bin_val)):
                if bin_val[inp_ix] == '0':
                    logging.info('i8.{}: input {} INACTIVE,'
                                        .format((test_ix * 2) + i8_ix + 1, inp_ix + 1))
                