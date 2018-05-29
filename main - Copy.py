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

class MainWindow(QtWidgets.QMainWindow):
    update_view_state_changed = QtCore.pyqtSignal(int)
    
    fname_1 = ""
    fname_2 = ""
    fname_3 = ""
    
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        uic.loadUi(
            os.path.join(os.path.split(__file__)[0], "parc.ui"),
            self)
        #self.initUi()
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
