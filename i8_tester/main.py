import sys
import time
from i2c_controller import Controller

ORDERLY = 1
RND = 2


def main():
    controller = Controller()
    
    # n = len(sys.argv)
    # print("Total arguments passed:", n)
    # print("\nArguments passed:", end = " ")

    # for i in range(1, n):
    #     print(sys.argv[i], end = " ")
    #     print("\n")

    # # if n != 3 and n != 5: 
    #     # return 0
        
    # if sys.argv[1] == '-n':
    #     print("number of trials to run: ", sys.argv[2])    
    #     trials = int(sys.argv[2])
    
    # if sys.argv[3] == '-s':
    #     if sys.argv[4]:
    #         test_type = sys.argv[4]

    # if sys.argv[5] == '-t':
    #     if sys.argv[6] and sys.argv[7]:
    #         active_delay = controller.set_open_delay[sys.argv[6],sys.argv[4]]
    #         # active_dur = controller.set_open_delay[sys.argv[7],sys.argv[4]]
            
   
    # sequence = controller.get_output_sequence(test_type)
# ---------------------------------------------------------------

    # for addr_ix in range(len(controller.I8_PAIR_ADDR)):
    for addr_ix in range(1):

        controller.set_pcf_address(3)

        for i in range(len(controller.I0_ADDR)):
            
            controller.word_reg[addr_ix][0] = 0xfd #controller.I0_ADDR[i]
            controller.word_reg[addr_ix][1] = 0xff
            controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
            print('PCF ADDR {} Port {} enabled'
                  .format(controller.I8_PAIR_ADDR[addr_ix],i))
            time.sleep(1)
        
        for i in range(len(controller.I0_ADDR)):
            controller.word_reg[addr_ix][0] = 0xff
            controller.word_reg[addr_ix][1] = 0xfd
            controller.i2c.write(bytearray(controller.word_reg[addr_ix]))
            print('PCF ADDR {} Port {} enabled'
                  .format(controller.I8_PAIR_ADDR[addr_ix] ,8 + i))
            time.sleep(1)

        controller.word_reg[addr_ix][0] = 0xff
        controller.word_reg[addr_ix][1] = 0xff
        controller.i2c.write(bytearray([controller.word_reg[addr_ix][0],\
                                   controller.word_reg[addr_ix][1]]))


#---------------------------------------------------------------


    # #-------------- Start of test -------------------
    # trials_count = trials
    # while trials_count:    
    #     for out in sequence:
    #         controller.write(out)
    #         time.sleep(active_dur)

    #         disable_out = ~out
    #         controller.write(disable_out)
    #         time.sleep(active_delay)
    


    #     trials_count -= 1

    # #------------- End of test ---------------------





if __name__ == '__main__':
    sys.exit(main())