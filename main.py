#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import datetime
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QAction, QFileDialog, QApplication)
import pyqtgraph
from Parcer import Pars
import numpy as np
import datetime
from PyQt5.QtCore import QTime, QTimer
pyqtgraph.setConfigOption('background', 'w')
pyqtgraph.setConfigOption('foreground', 'k')

#class TimeAxisItem(pyqtgraph.AxisItem):
   # def __init__(self, *args, **kwargs):
   #super().__init__(*args, **kwargs)

   #def tickStrings(self, values, scale, spacing):
   # PySide's QTime() initialiser fails miserably and dismisses args/kwargs
   #  return [useful_values_dict['useful_data']['data']['ISO_dates']]

class MainWindow(QtWidgets.QMainWindow):
    update_view_state_changed = QtCore.pyqtSignal(int)
    
    fname_1 = ""
    fname_2 = ""
    fname_3 = ""
    name_f1 = ""
    name_f2 = ""
    name_f3 = ""
    
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        uic.loadUi(
            os.path.join(os.path.split(__file__)[0], "untitled.ui"),
            self)
        self.initUi()        

    def initUi(self):
        
        self.pushButton.clicked.connect(self.showData)
        self.pushButton_2.clicked.connect(self.Clear)
        self.pushButton.setEnabled(False)
        self.actionOpen_File_1.triggered.connect(self.GetFile)
        #self.actionECEFtoENU.triggered.connect(seld.ECEFtoENU)
        self.actionOpen_File_2.triggered.connect(self.GetFile_1)
        self.actionOpen_File_3.triggered.connect(self.GetFile_2)
        self.actionExit.triggered.connect(self.Exit)
        self.actionExit.setShortcut('Ctrl+Q')
        self.Widget.showGrid(x = True, y = True)
        self.Widget.setLabel('bottom', 'Time(sec)')
       
        
    def GetFile(self):
        MainWindow.fname_1 = QFileDialog.getOpenFileName(self, 'Open file')
        MainWindow.fname_1 = MainWindow.fname_1[0]
        if MainWindow.fname_1 != "" or MainWindow.fname_2 != "" or MainWindow.fname_3 !="":
            self.pushButton.setEnabled(True)
        if MainWindow.fname_1 != "":
            MainWindow.name_f1 = (MainWindow.fname_1.split('/'))
            self.comboBox.addItem(MainWindow.name_f1[(len(MainWindow.fname_1.split('/')))-1])
      
    def GetFile_1(self):
        
        MainWindow.fname_2 = QFileDialog.getOpenFileName(self, 'Open file')
        MainWindow.fname_2 = MainWindow.fname_2[0]
        
        if MainWindow.fname_1 != "" or MainWindow.fname_2!= "" or MainWindow.fname_3 !="":
            self.pushButton.setEnabled(True)
        if MainWindow.fname_2 != "":
            MainWindow.name_f2 = (MainWindow.fname_2.split('/'))
            self.comboBox.addItem(MainWindow.name_f2[(len(MainWindow.fname_2.split('/')))-1])
            
    def GetFile_2(self):
        MainWindow.fname_3 = QFileDialog.getOpenFileName(self, 'Open file')
        MainWindow.fname_3 = MainWindow.fname_3[0]
        if MainWindow.fname_1 != "" or MainWindow.fname_2 != "" or MainWindow.fname_3 !="":
            self.pushButton.setEnabled(True)
        if MainWindow.fname_3 != "":
            MainWindow.name_f3 = (MainWindow.fname_3.split('/'))
            self.comboBox.addItem(MainWindow.name_f3[(len(MainWindow.fname_3.split('/')))-1])     

    def showData(self):
        
        obj1=Pars()
        self.Widget.addLegend()
        
        if self.checkBox.isChecked:
                   
            self.Widget.setLabel('left', 'Roll(deg)')
            if MainWindow.fname_1 != "":
                if self.comboBox.currentText() == MainWindow.name_f1[(len(MainWindow.fname_1.split('/')))- 1] and self.comboBox.currentText() != "":
                    obj1.parcer_1(MainWindow.fname_1)
                    self.Widget.plot(obj1.tm_1,obj1.roll_1,pen = pyqtgraph.mkPen(color='r', width=2),name = MainWindow.name_f1[(len(MainWindow.fname_1.split('/')))-1])
            if MainWindow.fname_2 != "":          
                if self.comboBox.currentText() == MainWindow.name_f2[(len(MainWindow.fname_2.split('/')))-1]  and self.comboBox.currentText() != "":
                   obj1.parcer_2(MainWindow.fname_2)
                   self.Widget.plot(obj1.tm_2,obj1.roll_2,pen = pyqtgraph.mkPen(color='r', width=2),name = MainWindow.name_f2[(len(MainWindow.fname_2.split('/')))-1])
            if MainWindow.fname_3 != "":
                if self.comboBox.currentText() == MainWindow.name_f3[(len(MainWindow.fname_3.split('/')))-1] and MainWindow.fname_3 != "":
                   obj1.parcer_3(MainWindow.fname_3)
                   self.Widget.plot(obj1.tm_3,obj1.roll_3,pen = pyqtgraph.mkPen(color='r', width=2),name = MainWindow.name_f3[(len(MainWindow.fname_3.split('/')))-1])
         

                
                         
       # if self.checkBox_2.isChecked() and MainWindow.fname_1 != "":
        #    pass
##            self.Widget.setLabel('left', 'Heading(deg)')
##  `          if self.comboBox.currentText() == MainWindow.name_f1[(len(MainWindow.fname_1.split('/')))-1]:
##                self.Widget.plot(obj1.tm_1,obj1.heading_1,pen = pyqtgraph.mkPen(color='r', width=2),name = MainWindow.name_f1[(len(MainWindow.fname_1.split('/')))-1])
##            if self.comboBox.currentText() == MainWindow.name_f2[(len(MainWindow.fname_2.split('/')))-1]:
##                self.Widget.plot(obj1.tm_2,obj1.heading_2,pen = pyqtgraph.mkPen(color='r', width=2),name = MainWindow.name_f2[(len(MainWindow.fname_2.split('/')))-1])
##            if self.comboBox.currentText() == MainWindow.name_f3[(len(MainWindow.fname_3.split('/')))-1]:
##                self.Widget.plot(obj1.tm_3,obj1.heading_3,pen = pyqtgraph.mkPen(color='r', width=2),name = MainWindow.name_f3[(len(MainWindow.fname_3.split('/')))-1])
##            self.Widget.plot(obj1.tm_1,obj1.heading_1,pen = pyqtgraph.mkPen(color='r', width=2),name='ref')
##          
            
           #self.widget.plot(clear=True) 

            #  xax = self.widget.getAxis('bottom')
            #def tickStrings(self,obj1.sm,scale,spacing):
            #return  obj1.sm

           # ticks = [list(zip(range(len(obj1.tm)),(obj1.sm)))]
         #   xax.setTicks(ticks)
            #f= xax.tickStrings(obj1.tm,1,10)
            #print(f)
            #self.widget.getAxis('bottom').setTickSpacing(50, 1)
         #   self.widget.plot(range(len(obj1.tm)),obj1.roll, pen = 'b')

        if self.checkBox_3.isChecked():
            pass
  
            #self.widget.setLabel('left', 'Latitude', units = 'd')
            #self.widget.setLabel('bottom', 'Time', units = 's')
            #self.widget.plot(obj1.u_tm,obj1.lat, pen = 'b')
           # self.widget.plot(obj1.u_tm,obj1.head, pen = 'b')
            #self.widget.plot(obj1.tm_1,obj1.heading_1,pen = pyqtgraph.mkPen(color='r', width=5),name='ref')                   
            
       
        if self.checkBox_4.isChecked():
            
            self.Widget.setLabel('left', 'Longitude', units = 'd')
            #self.widget.plot(obj1.u_tm,obj1.head, pen = 'r')

        if self.checkBox_5.isChecked():
            #self.widget.plot(obj1.u_tm_1,obj1.head_1,pen = pyqtgraph.mkPen(color='y', width=2),name='auto')
            self.Widget.plot(obj1.u_tm_2,obj1.head_2,pen = pyqtgraph.mkPen(color='b', width=2),name='auto')
            self.Widget.plot(obj1.u_tm_3,obj1.head_3,pen = pyqtgraph.mkPen(color='g', width=2),name='egn')

        if self.checkBox_6.isChecked():
           
            
            self.Widget.plot(obj1.u_tm_2,obj1.head_2,pen = pyqtgraph.mkPen(color='b', width=2),name='auto')
            self.Widget.plot(obj1.u_tm_3,obj1.head_3,pen = pyqtgraph.mkPen(color='g', width=2),name='egn')

       
    def Clear(self):
        self.Widget.plot(clear=True)
        
    def Exit(self):
        self.actionExit(sys.exit())
                
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
