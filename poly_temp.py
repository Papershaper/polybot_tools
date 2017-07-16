import requests
import os
import time
import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor_file = '/sys/bus/w1/devices/10-000802e80d45/w1_slave'
dweet_addr = 'https://dweet.io/dweet/for/'
dweet_name = 'polybot3_telemetry'
dweet_key = 'external_temp'

outage_count = 0
ten_max = -100.0
ten_min = 100.0

def temp_raw():
    f = open(temp_sensor_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return datetime.datetime.now().isoformat(), temp_c

def dweet_data(data):
    rqsStr = dweet_addr+dweet_name+ '?' +dweet_key+ '=' + str(data[1])
    try:
        rqs = requests.get(rqsStr)
    except ConnectionError:
        outage_count = outage_count+1
        print('Connection Error: ' + outage_count)

def temp_stats(temp):
    global ten_max, ten_min
    if ten_max < temp:
        ten_max = temp
    if ten_min > temp:
        ten_min = temp

print('Temp Sensor Initialized')
while True:
    temp_data = read_temp()
    temp_stats(temp_data[1])
    dweet_data(temp_data)
    print(temp_data[0] +" Temp:{0:4.2f}  Max:{1:4.2f} Min: {2:4.2f}".format(temp_data[1],ten_max,ten_min))
    time.sleep(60)
