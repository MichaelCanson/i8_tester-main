import mraa as m
import sys



def main():
    i2c = m.I2c(0,True)
    i2c.address(0x24)

    i2c.writeWordReg(0x42,0x0001)



if __name__ == '__main__':
    sys.exit(main())