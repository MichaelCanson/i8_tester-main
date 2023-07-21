import mraa as m
import sys
import time


def main():
    i2c = m.I2c(2,True)
    io_addr= [0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f]

    i2c.address(0x20)
    trial = int(sys.argv[1])
    for t in range(trial):
        for i in io_addr:
            i2c.write(bytearray([i,0xff]))
            time.sleep(1)
            
    i2c.write(bytearray([0xff,0xff]))
    # for i in range(trial):
    #     i2c.write(bytearray([0x00,0x00]))
    #     print('PFC Board all ON')
    #     time.sleep(3)
    #     i2c.write(bytearray([0xff,0xff]))
    #     print('PCF Board all OFF')
    #     time.sleep(3)

    print('Test done.')

if __name__ == '__main__':
    sys.exit(main())