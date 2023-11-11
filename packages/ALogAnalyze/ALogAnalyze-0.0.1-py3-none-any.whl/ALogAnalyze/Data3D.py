#!/usr/bin/env python3

import datetime

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D

from ALogAnalyze.UI import *
from ALogAnalyze.Config import UIGridLayout

import VisualLog.LogParser as LogParser
import VisualLog.MatplotlibZoom as MatplotlibZoom

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Data3D:

    def __init__(self, ui: Ui_MainWindow, MainWindow: QMainWindow,  config: dict):
        self.ui = ui
        self.config = config
        self.MainWindow = MainWindow

        self.gridLayout = UIGridLayout(self.config["Data3D"], self.MainWindow, self.ui.D3DTypesComboBox, self.ui.D3DGridLayout)
        self.ui.D3DRunPushButton.clicked.connect(self.D3DRunClick)
        self.ui.D3DParsePushButton.clicked.connect(self.D3DParseClick)

    def D3DParseClick(self):
        print("D3DParseClick")

        keyValues: dict = self.gridLayout.getInfoData()
        print(keyValues)

        self.D3DParseData(keyValues)

    def D3DParseData(self, keyValues: dict):
        self.ui.D3DInfoPlainTextEdit.clear()

        lineInfos = LogParser.logFileParser(
                keyValues["File Path"],
                # r'(\d+)\s+(\d+)\s+(\d+)',
                keyValues["Data Regex"]
            )
        
        for info in lineInfos:
            # print(info)
            line = ""
            for i in range(len(info)):
                if isinstance(info[i], datetime.datetime):
                    line += info[i].strftime("%Y-%m-%d %H:%M:%S.%f") + ", "
                elif i == (len(info) - 1):
                    line += str(info[i])
                else:
                    line += str(info[i]) + ", "

            self.ui.D3DInfoPlainTextEdit.appendPlainText(line)
        
        return lineInfos

    def D3DRunClick(self):
        print("D3DRunClick")

        keyValues = self.gridLayout.getInfoData()
        lineInfos = self.D3DParseData(keyValues)
        MatplotlibZoom.Show(callback=self.defaultShowCallback, rows = 1, cols = 1, d3=True, args=[lineInfos, keyValues])

        # fig: Figure = plot.figure()
        # ax: Axes3D = fig.add_subplot(111, projection='3d')
        # ax.cla()
        # # ax = plt.axes(projection='3d')
        # ax.set_xlabel('x-axis')
        # ax.set_ylabel('y-axis')
        # ax.set_zlabel('z-axis')
        # ax.view_init(elev=45, azim=45)

        # # ValueError: data type must provide an itemsize
        # # 输入的数据是字符串导致，需要整形、浮点型数据
        # # 
        # # b: blue
        # # c: cyan
        # # g: green
        # # k: black
        # # m: magenta
        # # r: red
        # # w: white
        # # y: yellow

        # # start point with other
        # ax.scatter3D(lineInfos[0][0], lineInfos[0][1], lineInfos[0][2], cmap='b')
        # ax.scatter3D([s[0] for s in lineInfos[1:]], [s[1] for s in lineInfos[1:]], [s[2] for s in lineInfos[1:]], cmap='r')
        # # line
        # ax.plot3D([s[0] for s in lineInfos], [s[1] for s in lineInfos], [s[2] for s in lineInfos], 'gray')

        # plot.show()

    def defaultShowCallback(self, fig: Figure, index, args=[]):
        if len(args) <= 0:
            return

        lineInfos = args[0]
        keyValues = args[1]
        dataIndex = eval("[" + keyValues["Data Index"].strip() + "]")
        x = dataIndex[0]
        y = dataIndex[1]
        z = dataIndex[2]

        ax: Axes3D = fig.get_axes()[index]

        # ax = plt.axes(projection='3d')
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')
        ax.view_init(elev=45, azim=45)

        # ValueError: data type must provide an itemsize
        # 输入的数据是字符串导致，需要整形、浮点型数据
        # 
        # b: blue
        # c: cyan
        # g: green
        # k: black
        # m: magenta
        # r: red
        # w: white
        # y: yellow

        # start point
        ax.scatter3D(lineInfos[0][x], lineInfos[0][y], lineInfos[0][z], cmap='b')
        # second pointer with other
        ax.scatter3D([s[x] for s in lineInfos[1:]], [s[y] for s in lineInfos[1:]], [s[z] for s in lineInfos[1:]], cmap='r')
        # line
        ax.plot3D([s[x] for s in lineInfos], [s[y] for s in lineInfos], [s[z] for s in lineInfos], 'gray')
