'''
Copyright(c) 2023 Marquis Systems Inc.

'''
import time
import mraa 
import random
import i2c_defs
class Controller():

    def __init__(self):
        
        self.i2c = mraa.I2c(i2c_defs.BUS_ADDR,True)
        self.current_addr = i2c_defs.I8_PAIR_ADDR[0]
        
        self.curr_pin = 0xff
        self.word_reg = i2c_defs.WORD_REG
        self.close_delay = 0
        self.open_duration = 0


    def set_pcf_address(self,index):
        self.current_addr = i2c_defs.I8_PAIR_ADDR[index]
        print('current PCF Address: {}'.format(hex(self.current_addr)))
        self.i2c.address(self.current_addr)


    def set_open_delay(self,sec):
        self.delay = sec


    def set_open_dur(self, sec):
        self.open_duration = sec
