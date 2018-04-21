import time, DAN, requests
from random import *

ServerIP = '140.113.199.204' #Change to your IoTtalk IP or None for autoSearching
Reg_addr='0516310' #None # if None, Reg_addr = MAC address

DAN.profile['dm_name']='0516310'
DAN.profile['df_list']=['0516310']
DAN.profile['d_name']= None # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)

while True:
    try:
    #Pull data from a device feature called "Dummy_Control"
        value1 = DAN.pull('0516310')
        if value1 != None and value1 != [None]:
            if value1[0] == 1:
                print('up')
            else :
                print('down')


    #Push data to a device feature called "Dummy_Sensor"
    #    value2=randint(1, 100)
    #    DAN.push ('Dummy_Sensor', value2)

    except Exception as e:
        print(e)
        DAN.device_registration_with_retry(ServerIP, Reg_addr)

    time.sleep(0.2)
