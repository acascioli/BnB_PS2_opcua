from gui.core.ua_client import UaClient
from qt_core import *
from gui.core.functions import Functions

from collections import namedtuple
import collections
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns
import random
import sys
import time

matplotlib.use('Qt5Agg')

t = []
# ram_2 = collections.deque(np.zeros(10))


class MatplotlibWidget(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, stram=True, plt_twin_1=True, plt_twin_2=True):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.stram = stram
        self.plt_twin_1 = plt_twin_1
        self.plt_twin_2 = plt_twin_2
        self.ax = fig.add_subplot(111)
        fig.subplots_adjust(right=0.75)
        self.twin1 = self.ax.twinx()
        self.twin2 = self.ax.twinx()

        self.ax.autoscale(enable=True)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)
        # self.toolbar = NavigationToolbar(self, self)

    def set_stram(self, value):
        self.stram = value


class DynamicWidget(MatplotlibWidget):
    def set_data_y(self, t, lbls_y, dataDict, clrs):
        self.tkw = dict(size=4, width=1.5)
        self.ax.clear()
        self.ax.autoscale(enable=True)
        self.ax.set_xlabel('Time [s]')
        self.ax.set_ylabel('T [°C]')
        self.ax.set_title('My Data')

        for i, lbl in enumerate(lbls_y):
            y = dataDict[lbl]
            p1, = self.ax.plot(t, y, color=clrs[i], label=lbl)
            self.ax.scatter(t[-1], y[-1])
            self.ax.text(t[-1], y[-1]+2, "{}".format(y[-1]))
            self.ax.yaxis.label.set_color(p1.get_color())
            self.ax.tick_params(axis='y', colors=p1.get_color(), **self.tkw)
            self.ax.tick_params(axis='x', **self.tkw)
        self.ax.set_ylim(0, y[-1]+10)
        self.ax.legend(loc=9)

    def set_data_twin_1(self, t, lbls_twin_1, dataDict, clrs):
        self.twin1.clear()
        self.twin1.autoscale(enable=True)
        self.twin1.set_ylabel("P [bar]")
        if len(lbls_twin_1) > 0:
            for i, lbl in enumerate(lbls_twin_1):
                y = dataDict[lbl]
                p2, = self.twin1.plot(t, y, color=clrs[i], label=lbl)
                self.twin1.scatter(t[-1], y[-1])
                self.twin1.text(t[-1], y[-1]+2, "{}".format(y[-1]))
                self.twin1.yaxis.label.set_color(p2.get_color())
                self.twin1.tick_params(
                    axis='y', colors=p2.get_color(), **self.tkw)
            self.twin1.set_ylim(0, y[-1]+10)
            self.twin1.legend(loc=1)
        else:
            p2, = self.twin1.plot([], [])

    def set_data_twin_2(self, t, lbls_twin_2, dataDict, clrs):
        self.twin2.clear()
        self.twin2.spines.right.set_position(("axes", 1.2))
        self.twin2.autoscale(enable=True)
        self.twin2.set_ylabel("Flow [ml/min]")
        if len(lbls_twin_2) > 0:
            for i, lbl in enumerate(lbls_twin_2):
                y = dataDict[lbl]
                p3, = self.twin2.plot(t, y, color=clrs[i], label=lbl)
                self.twin2.scatter(t[-1], y[-1])
                self.twin2.text(t[-1], y[-1]+2, "{}".format(y[-1]))
                self.twin2.yaxis.label.set_color(p3.get_color())
                self.twin2.tick_params(
                    axis='y', colors=p3.get_color(), **self.tkw)
            self.twin2.set_ylim(0, y[-1]+10)
            self.twin2.legend(loc=2)
        else:
            p2, = self.twin2.plot([], [])


class RandomDataWidget(DynamicWidget):
    def __init__(self, *args, **kwargs):
        DynamicWidget.__init__(self, *args, **kwargs)
        timer = QTimer(self)
        # timer.timeout.connect(self.generate_and_set_data)
        timer.start(500)

    def init_dict(self, subdf):
        self.dataDict = {}
        for id, row in subdf.iterrows():
            self.dataDict[row['VISUALIZATION NAME']] = []
        self.dataDict['t'] = []

    def plt_vals(self, subdf):
        group_y = ['Temp', 'PID1', 'PID3', 'PID4', 'PID5']
        palette = 'deep'
        n_of_colors = len(subdf)
        clrs = sns.color_palette(palette, n_of_colors)
        len_y = len(subdf[(subdf['Group'].isin(group_y))])
        clrs_y = clrs[:len_y]
        group_twin_1 = ['PID']
        len_twin_1 = len(subdf[(subdf['Group'].isin(group_twin_1))])
        clrs_twin_1 = clrs[len_y:(len_y+len_twin_1)]
        group_twin_2 = ['PUMP']
        len_twin_2 = len(subdf[(subdf['Group'].isin(group_twin_2))])
        clrs_twin_2 = clrs[(len_y+len_twin_1):(len_y+len_twin_1+len_twin_2)]

        start_time = 0
        t.append(time.process_time() - start_time)
        self.dataDict['t'].append(time.process_time() - start_time)

        for id, row in subdf.iterrows():
            self.dataDict[row['VISUALIZATION NAME']].append(row['Values'])


        lbls_y = subdf[(subdf['Group'].isin(group_y)) & (
            subdf['Plot'] == True)]['VISUALIZATION NAME'].tolist()

        lbls_twin_1 = subdf[(subdf['Group'].isin(group_twin_1)) & (
            subdf['Plot'] == True)]['VISUALIZATION NAME'].tolist()

        lbls_twin_2 = subdf[(subdf['Group'].isin(group_twin_2)) & (
            subdf['Plot'] == True)]['VISUALIZATION NAME'].tolist()

        if self.stram:
            self.set_data_y(t, lbls_y, self.dataDict, clrs_y)
            self.set_data_twin_1(t, lbls_twin_1, self.dataDict, clrs_twin_1)
            self.set_data_twin_2(t, lbls_twin_2, self.dataDict, clrs_twin_2)

            self.ax.figure.canvas.draw()
            self.ax.figure.canvas.flush_events()

        return self.dataDict
