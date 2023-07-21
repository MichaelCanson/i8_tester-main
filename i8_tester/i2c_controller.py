import time
import mraa 
import random
class Controller():

    BUS_ADDR = 0x02
    I8_PAIR_ADDR = [0x20,0x21,0x22,0x23] #PCF address with constant pcf value and LSB: R/W bit set to 1.
    # WORD_REG = [(0xff,0xff),(0xff,0xff),(0xff,0xff),(0xff,0xff)] 
    I0_ADDR = [0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f]
    
    
    def __init__(self):

        self.i2c = mraa.I2c(Controller.BUS_ADDR,True)
        self.out_on = 0x00
        self.out_off = ~self.out_on
        self.curr_pin = 0x01
        self.close_delay = 0
        self.open_duration = 0
        self.out_sequence = []
        self.word_reg = [[0xff,0xff],[0xff,0xff],\
                         [0xff,0xff],[0xff,0xff],] 


    def set_pcf_address(self,index):
        self.current_addr = Controller.I8_PAIR_ADDR[index]
        print('current PCF Address: {}'.format(hex(self.current_addr)))
        self.i2c.address(self.current_addr)


    def set_open_delay(self,sec, test_type):
        if test_type == 1:
            self.delay = sec

        elif test_type == 2:
            self.delay = random.randint(1,8)


    def set_open_dur(self, sec, test_type):
        if test_type == 1:
            self.open_duration = sec

        elif test_type == 2:
            self.open_duration = random.randint(1,8)
        
        return sec

    
    def get_output_sequence(self, test_type):
        print('pos: {}'.format(test_type))
        if test_type == 1:  #from i8.1 to i4
            print('GOS - Test Type: activate single input one at a time.')
            pin_sequence = Controller.I0_ADDR

        elif test_type == 2:
            pass

        elif test_type == 3:
            pass

        elif test_type == 4:
            pass

        return pin_sequence


    

    # def in_sequence(self):
     
    #     for pin in range(len(Controller.I0_ADDR)):
    #         self.curr_pin = Controller.I0_ADDR[pin]
    #         print('self.curr_pin_ON[0]: {}'.format(hex(self.curr_pin)))
    #         self.write(self.curr_pin)

    #         time.sleep(self.delay)

    #         self.curr_pin = (self.curr_pin) & (~self.curr_pin)
    #         print('self.curr_pin_OFF[0]: {}\n'.format(self.curr_pin))
    #         self.write(self.curr_pin)

    #         time.sleep(self.delay)
