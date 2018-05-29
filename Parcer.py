# -*- coding: utf-8 -*-
import datetime
import time
import pyqtgraph as pg
import numpy as np
from PyQt5 import QtGui
from PyQt5 import QtCore

class Pars:
    def __init__(self):

        self.roll_1 = []
        self.roll_2 = []
        self.roll_3 = []
        self.heading_1 = []
        self.heading_2 = []
        self.heading_3 = []
        self.tm_1 = []
        self.tm_2 = []
        self.tm_3 = []
        self.sm = []
        self.u_tm = []
        self.u_tm_2 = []
        self.u_tm_3 = []
        self.lat = []
        self.lon = []
        self.head = []
        self.head_2 = []
        self.head_3 = []
        self.time = ""
# переназвать для второго файла
    def parcer_1(self,fname_1):

        self.fname_1 = fname_1
        if fname_1 != "":
            f = open(fname_1)
        for i, line in enumerate(f):
            if "PTPSR" in line:
                if "*" in line: 
                    #print("line %s: %s" % (i, line, ))
                    _id, msg_type, validation, time, heading, roll, sol_type, rms_h, rms_r_crc = line.split(',')
                    h = float(heading)
                    convert = (lambda h: h + 90 if h < 270 else h - 270)

                    self.heading_1.append(convert(h))
															
                    self.roll_1.append(float(roll))
                    self.tm_1.append(float(time))
                    hour = (time[0:2])
                    minute = (time[2:4])
                    second = (time[4:6])
                    microsecond = (time[7:9])
                    a = (hour + ":" + minute + ":" + second + ":" + microsecond)
                    self.sm.append(a)
                    #print(time)
                        
            if "GNRMC" in line:
                if "*" in line:
                    (_id, utc_time, pos_state, lat, lat_hem, lon,lon_hem, speed, head, date, mag_var, mag_dir,os_mode_crc) = line.split(',')
                    self.u_tm.append(float(utc_time))
                    self.lat.append(float(lat))
                    self.lon.append(float(lon))
                    self.head.append(float(head))
               #datetime.strptime(a)
               #b = datetime.time(hour=hour, minute=minute, second=second, microsecond=microsecond)
               #c = datetime.strptime(hour+":"+minute+":"+ second + ":" +microsecond)
               #print(c)
      
    def parcer_2(self,fname_2):
        
        self.fname_2 = fname_2
        if fname_2 != "":
            b = open(fname_2)
            for i, line in enumerate(b):

                if "PTPSR" in line:
                    if "*" in line: 
                    #print("line %s: %s" % (i, line, ))
                        _id, msg_type, validation, time, heading, roll, sol_type, rms_h, rms_r_crc = line.split(',')
                        self.heading_2.append(float(heading))
                        self.roll_2.append(float(roll))
                        self.tm_2.append(float(time))
                        hour = (time[0:2])
                        minute = (time[2:4])
                        second = (time[4:6])
                        microsecond = (time[7:9])
                        a = (hour+":"+minute+":"+second+":"+microsecond)
                        self.sm.append(a)
                    #print(time)                                               
                if "GNRMC" in line:
                    if "*" in line:
                        (_id, utc_time, pos_state, lat, lat_hem, lon,lon_hem, speed, head, date, mag_var, mag_dir,os_mode_crc) = line.split(',')
                        self.u_tm_2.append(float(utc_time))
                        self.lat.append(float(lat))
                        self.lon.append(float(lon))
                        self.head_2.append(float(head))
               #datetime.strptime(a)
               #b = datetime.time(hour=hour, minute=minute, second=second, microsecond=microsecond)
               #c = datetime.strptime(hour+":"+minute+":"+ second + ":" +microsecond)
               #print(c)
    def parcer_3(self,fname_3):
        
        self.fname_3 = fname_3
        if fname_3 != "":
            d = open(fname_3)
            for i, line in enumerate(d):

                if "PTPSR" in line:
                    if "*" in line: 
                    #print("line %s: %s" % (i, line, ))
                        _id, msg_type, validation, time, heading, roll, sol_type, rms_h, rms_r_crc = line.split(',')
                        self.heading_3.append(float(heading))
                        self.roll_3.append(float(roll))
                        self.tm_3.append(float(time))
                        hour = (time[0:2])
                        minute = (time[2:4])
                        second = (time[4:6])
                        microsecond = (time[7:9])
                        a = (hour+":"+minute+":"+second+":"+microsecond)
                        self.sm.append(a)
                    #print(time)                                               
                if "GNRMC" in line:
                    if "*" in line:
                        (_id, utc_time, pos_state, lat, lat_hem, lon,lon_hem, speed, head, date, mag_var, mag_dir,os_mode_crc) = line.split(',')
                        self.u_tm_3.append(float(utc_time))
                        self.lat.append(float(lat))
                        self.lon.append(float(lon))
                        self.head_3.append(float(head))
          
if __name__ == "__main__":
    roll = []
    heading = []
    tm = []
    obj1=Pars()
    obj1.parcer_1('new2.txt')
    #print(len(obj1.roll))


    
       





