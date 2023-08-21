from i2c_controller import Controller
import i2c_defs
import csv
import sys

def main():
    log_title = '2023-08-15(7)'
    test_log = '{}/{}.txt'.format(i2c_defs.FILE_PATH,log_title)
    
    csv_log = '{}/{}.csv'.format(i2c_defs.CSV_PATH,log_title)
    with open(test_log,'r') as input_file:
        print('test log opened succesfully')
        stripped = (line.strip() for line in input_file)
        lines = (line.split(",") for line in stripped if line)
        with open(csv_log, 'w') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(('Timestamp','iSTAR i8','Input Port'))
            writer.writerows(lines)



if __name__ == '__main__':
    sys.exit(main())