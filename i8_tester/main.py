import sys
import time
from i2c_controller import Controller

ORDERLY = 1
RND = 2


def main():
    controller = Controller()
    
    n = len(sys.argv)
    print("Total arguments passed:", n)
    print("\nArguments passed:", end = " ")

    for i in range(1, n):
        print(sys.argv[i], end = " ")
        print("\n")

    if n != 3 and n != 5: 
        return 0
        
    if sys.argv[1] == '-n':
        print("number of trials to run: ", sys.argv[2])    
        trials = int(sys.argv[2])
    
    if sys.argv[3] == '-s':
        if sys.argv[4]:
            test_type = sys.argv[4]

    if sys.argv[5] == '-t':
        if sys.argv[6] and sys.argv[7]:
            active_delay = controller.set_open_delay[sys.argv[6],sys.argv[4]]
            active_dur = controller.set_open_delay[sys.argv[7],sys.argv[4]]
            
   
    sequence = controller.get_output_sequence(test)
    #-------------- Start of test -------------------
    trials_count = trials
    while trials_count:
            
        for out in sequence:
            controller.write(out)
            time.sleep(active_dur)

            disable_out = ~out
            controller.write(disable_out)
            time.sleep(active_delay)
    


        trials_count -= 1

    #------------- End of test ---------------------





if __name__ == '__main__':
    sys.exit(main())