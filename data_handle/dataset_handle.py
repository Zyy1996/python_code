import os
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

class Table_drawing:
    def __init__(self, data_type, title_lab) -> None:
        self.data = []
        self.data_type = data_type
        self.app = pg.mkQApp("Plotting")
        self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.win.resize(1000, 600)
        self.win.setWindowTitle('消耗统计')

        pg.setConfigOptions(antialias=True)
        self.p6 = self.win.addPlot(title=title_lab)
        self.p6.addLegend()
        self.p6.showGrid(y=1)
        self.p6.setLabel("bottom", "运行时间", "s")
        self.p6.setLabel("left", "cpu消耗", "%")
        self.curve = self.p6.plot(pen='y')

    def table_drawing_get_data(self, data):
        if self.data_type == 1:
            self.data.append(int(data))
        else:
            print(self.data_type, "err")

    def table_drawing_finish(self):
        # print(self.data)
        self.curve.setData(self.data)
        pg.exec()

class Polt_draw:
    def __init__(self,data_type:int,title_lab:str,data:dict) -> None:
        self.data_type = data_type
        self.app = pg.mkQApp("Plotting")
        self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.win.resize(1000, 600)
        self.win.setWindowTitle('消耗统计')
        pg.setConfigOptions(antialias=True)
        self.win.setBackground((255,255,255))
        self.p1 = self.win.addPlot(title=title_lab)
        self.win.nextRow()
        self.p2 = self.win.addLabel("qqwqw")
        self.p1.showGrid(y=1)
        self.p1.setLabel("bottom", "运行时间", "s")
        self.p1.setLabel("left", "cpu消耗", "%")
        self.p1.setMouseEnabled(True,True)

        for key,value in data.items():
            if isinstance(value,list) and len(value) > 0:
                self.p1.plot(value, pen=(0,0,0), name=str(key))
            else:
                print("value err")
        self.p1.setAxisItems()

    def show(self):
        pg.exec()

if __name__ == '__main__':

    a = Polt_draw(0,"cpu消耗",{"data":123})
    a.show()
