from gui.core.ua_client import UaClient
from qt_core import *
from gui.core.functions import Functions

from collections import namedtuple
import collections
import psutil
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt
import matplotlib
import random
import sys
import time

matplotlib.use('Qt5Agg')


DataModel = namedtuple('DataModel', ['start_x', 'start_y', 'width', 'height'])

t = []
cpu = []
ram = []
ram_2 = []
# t = collections.deque(np.zeros(10))
# cpu = collections.deque(np.zeros(10))
# ram = collections.deque(np.zeros(10))
# ram_2 = collections.deque(np.zeros(10))


class MatplotlibWidget(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, stram=True, plt_twin_1=True, plt_twin_2=True):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.stram = stram
        self.plt_twin_1 = plt_twin_1
        self.plt_twin_2 = plt_twin_2
        self.axes = fig.add_subplot(111)
        fig.subplots_adjust(right=0.75)
        self.twin1 = self.axes.twinx()
        self.twin2 = self.axes.twinx()

        # Offset the right spine of twin2.  The ticks and label have already been
        # placed on the right by twinx above.
        self.twin2.spines.right.set_position(("axes", 1.2))

        self.axes.autoscale(enable=True)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)
        # self.toolbar = NavigationToolbar(self, self)

    def set_stram(self, value):
        self.stram = value

    def set_plt_twin_1(self, value):
        self.plt_twin_1 = value

    def set_plt_twin_2(self, value):
        self.plt_twin_2 = value


class DynamicWidget(MatplotlibWidget):
    def set_data(self, t, cpu, ram, ram_2, plt_twin_1, plt_twin_2):
        tkw = dict(size=4, width=1.5)
        self.axes.clear()
        self.twin1.clear()
        self.twin2.clear()
        self.twin2.spines.right.set_position(("axes", 1.2))
        self.axes.autoscale(enable=True)
        self.axes.set_xlabel('Time [s]')
        self.axes.set_ylabel('Y Label')
        self.axes.set_title('My Data')
        p1, = self.axes.plot(t, cpu, "b-", label="cpu")
        self.axes.scatter(t[-1], cpu[-1])
        self.axes.text(t[-1], cpu[-1]+2, "{}%".format(cpu[-1]))
        self.axes.yaxis.label.set_color(p1.get_color())
        self.axes.tick_params(axis='y', colors=p1.get_color(), **tkw)
        self.axes.tick_params(axis='x', **tkw)
        self.axes.set_ylim(0, 100)
        if plt_twin_1:
            self.twin1.autoscale(enable=True)
            self.twin1.set_ylabel("Twin 1 Label")
            p2, = self.twin1.plot(t, ram, "r-", label="ram")
            self.twin1.scatter(t[-1], ram[-1])
            self.twin1.text(t[-1], ram[-1]+2, "{}%".format(ram[-1]))
            self.twin1.yaxis.label.set_color(p2.get_color())
            self.twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
            self.twin1.set_ylim(0, 100)
            self.twin1.legend(loc=1)
        else:
            p2, = self.twin1.plot([], [])
        if plt_twin_2:
            self.twin2.autoscale(enable=True)
            self.twin2.set_ylabel("Twin 2 Label")
            p3, = self.twin2.plot(t, ram_2, "g-", label="ram_2")
            self.twin2.scatter(t[-1], ram_2[-1])
            self.twin2.text(t[-1], ram_2[-1]+2, "{}%".format(ram_2[-1]))
            self.twin2.yaxis.label.set_color(p3.get_color())
            self.twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
            self.twin2.set_ylim(0, 100)
            self.twin2.legend(loc=2)
        else:
            p3, = self.twin1.plot([], [])

        # if plt_twin_1 and plt_twin_2:
        self.axes.legend(loc=9)
        
        # self.axes.legend(handles=[p1, p2, p3])
        # else:
        #     self.axes.legend(handles=[p1, p3])

        self.axes.figure.canvas.draw()
        self.axes.figure.canvas.flush_events()


class RandomDataWidget(DynamicWidget):
    def __init__(self, *args, **kwargs):
        DynamicWidget.__init__(self, *args, **kwargs)
        timer = QTimer(self)
        timer.timeout.connect(self.generate_and_set_data)
        timer.start(500)

    def generate_and_set_data(self):
        start_time = 0
        # t.popleft()
        t.append(time.process_time() - start_time)
        # cpu.popleft()
        cpu.append(psutil.cpu_percent(interval=0.5))
        # ram.popleft()
        ram.append(psutil.virtual_memory().percent)
        # ram_2.popleft()
        ram_2.append(np.round(np.sqrt(psutil.virtual_memory().percent), 2))
        # print('self.plt_twin_1', self.plt_twin_1)
        if self.stram:
            self.set_data(t, cpu, ram, ram_2, self.plt_twin_1, self.plt_twin_2)
