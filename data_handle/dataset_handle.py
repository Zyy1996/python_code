import os
import sys
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

class Table_drawing():
    def __init__(self,data_type,title_lab) -> None:
        self.data = []
        self.data_type = data_type
        self.app = pg.mkQApp("Plotting Example")
        self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.win.resize(1000,600)
        self.win.setWindowTitle('pyqtgraph example: Plotting')
        
        pg.setConfigOptions(antialias=True)
        self.p6 = self.win.addPlot(title=title_lab)
        self.p6.addLegend()
        self.p6.showGrid(y=1)
        self.p6.setLabel("bottom","运行时间","s")
        self.p6.setLabel("left","cpu消耗","%")
        self.curve = self.p6.plot(pen='y')

    def table_drawing_get_data(self,data):
        if self.data_type == 1:
            self.data.append(int(data))
        else:
            print(self.data_type , "err")

    def table_drawing_finish(self):
        # print(self.data)
        self.curve.setData(self.data)
        pg.exec()

if __name__ == '__main__':
    a = Table_drawing(1)
    a.table_drawing_get_data(1)
    a.table_drawing_get_data(12)
    a.table_drawing_get_data(13)
    a.table_drawing_get_data(14)
    a.table_drawing_get_data(15)

    a.table_drawing_finish()
