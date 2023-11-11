#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#

import json
import os
import re
import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Config():

    def __new__(self):
        configFile = open(os.path.dirname(__file__) + '/template/config.json')
        config = json.load(configFile)
        # print(json.dumps(config, indent=4))

        return config

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S.%f')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def defaultLineCallback(lineInfo):
    lineInfoFixed = []
    today_year    = str(datetime.date.today().year)
    # print(lineInfo)

    for index in range(len(lineInfo)):
        data       = None
        dateRegex  = "(\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d*)"
        floatRegex = "[-]?\d*\.\d*"
        intRegex   = "[-]?\d+"

        datePattern       = re.compile(dateRegex)
        floatPattern      = re.compile(floatRegex)
        intPattern        = re.compile(intRegex)
        matchDatePattern  = datePattern.match(lineInfo[index])
        matchFloatPattern = floatPattern.match(lineInfo[index])
        matchIntPattern   = intPattern.match(lineInfo[index])

        if matchDatePattern:
            timeString = today_year + "-" + lineInfo[index]
            data = datetime.datetime.strptime(timeString, "%Y-%m-%d %H:%M:%S.%f")
        elif matchFloatPattern:
            data = eval("float(lineInfo[index].strip())")
        elif matchIntPattern:
            data = eval("int(lineInfo[index].strip())")
        else:
            data = lineInfo[index].strip()

        lineInfoFixed.append(data)

    return lineInfoFixed

class UIGridLayout():

    def __init__(self, config, mainWindow: QMainWindow, comboBox: QComboBox, gridLayout: QGridLayout):
        self.config = config
        self.mainWindow = mainWindow
        self.gridLayout = gridLayout
        self.comboBox = comboBox

        self.templates = []
        for i in self.config:
            self.templates.append(i["name"])

        self.comboBox.addItems(self.templates)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentIndexChanged.connect(self.typesChanged)

        self.filleGridLayout(0)

    def typesChanged(self):
        comboBoxIndex = self.comboBox.currentIndex()
        # fill gridlayout
        print("combobox: " + str(comboBoxIndex))
        self.filleGridLayout(comboBoxIndex)

    def getInfoData(self):
        keyValues = {}
        for i in range(self.gridLayout.rowCount()):
            if self.gridLayout.itemAtPosition(i, 0) == None:
                continue

            key = self.gridLayout.itemAtPosition(i, 0).widget().text()
            textEdit = self.gridLayout.itemAtPosition(i, 1).widget()
            if isinstance(textEdit, QTextEdit):
                value = textEdit.toPlainText().split("\n")
            else:
                value = textEdit.text()

            if key in ["File Path", "File Path:"] and ("/" in value or "\\" in value):
                if not os.path.exists(value):
                    if (os.path.exists("src/ALogAnalyze")):
                        value = "src/ALogAnalyze/" + value

                    if not os.path.exists(value):
                        value = os.path.dirname(__file__) + "/" + value

            keyValues[key] = value

        return keyValues

    def filleGridLayout(self, index: int):
        # keyValues = self.config[self.title][index]
        keyValues = self.config[index]
        i = 0

        item_list = list(range(self.gridLayout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序

        for i in item_list:
            item = self.gridLayout.itemAt(i)
            self.gridLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
 
        i = 0
        if "components" in keyValues.keys():
            '''
            {
                "name": "line",
                "components": [
                    {
                        "name": "File Path",
                        "fileSelect": true,
                        "uiType": "QLineEdit",
                        "valueType": "string",
                        "value": "template/hands.txt"
                    },
                    {
                        "name": "Data Regex",
                        "fileSelect": false,
                        "uiType": "QTextEdit",
                        "valueType": "string",
                        "value": "x\\s*=\\s*([-]?\\d.\\d+),\\s*y\\s*=\\s*([-]?\\d.\\d+),\\s*z\\s*=\\s*([-]?\\d.\\d+)"
                    },
                    {
                        "name": "Data Index",
                        "fileSelect": false,
                        "uiType": "QLineEdit",
                        "valueType": "string",
                        "value": "0, 1, 2"
                    }
                ]
            },
            '''
            for keyValue in keyValues["components"]:
                label = QLabel(keyValue["name"])

                if keyValue["uiType"] == "QTextEdit":
                    value = QTextEdit()
                    if isinstance(keyValue["value"], str):
                        value.setText(keyValue["value"])
                    else:
                        value.setText("\n".join(keyValue["value"]))
                    value.setMaximumHeight(90)
                elif keyValue["uiType"] == "QLineEdit":
                    value = QLineEdit(keyValue["value"])
                else:
                    value = QLineEdit(keyValue["value"])

                if keyValue["fileSelect"]:
                    button = QPushButton("Select File ...")
                    button.clicked.connect(self.fileSelectClicked)
                    self.gridLayout.addWidget(button, i, 2, 1, 1)

                self.gridLayout.addWidget(label, i, 0, 1, 1)
                self.gridLayout.addWidget(value, i, 1, 1, 1)

                i += 1
        else:
            '''
                {
                   "name": "line",
                   "File Path": "template/hands.txt",
                   "Data Regex": "x\\s*=\\s*([-]?\\d.\\d+),\\s*y\\s*=\\s*([-]?\\d.\\d+),\\s*z\\s*=\\s*([-]?\\d.\\d+)",
                   "Data Index": "0, 1, 2"
                },
            '''
            for key in keyValues.keys():
                if key == "name":
                    continue

                label = QLabel(key)

                if key == "Data Regex":
                    value = QTextEdit()
                    if isinstance(keyValues[key], str):
                        value.setText(keyValues[key])
                    else:
                        value.setText("\n".join(keyValues[key]))
                    value.setMaximumHeight(90)
                elif key == "File Path":
                    value = QLineEdit(keyValues[key])

                    button = QPushButton("Select File ...")
                    button.clicked.connect(self.fileSelectClicked)
                    self.gridLayout.addWidget(button, i, 2, 1, 1)
                else:
                    value = QLineEdit(keyValues[key])

                self.gridLayout.addWidget(label, i, 0, 1, 1)
                self.gridLayout.addWidget(value, i, 1, 1, 1)

                i += 1

    def fileSelectClicked(self):
        print("fileSelectClicked")

        row, col = self.findWidgetPosition(self.gridLayout)

        fileName,fileType = QFileDialog.getOpenFileName(None, "select file", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        if (len(fileName) > 0):
            print(fileName)
            print(fileType)

            edit: QLineEdit = self.gridLayout.itemAtPosition(row, col - 1).widget()
            edit.setText(fileName)

    def findWidgetPosition(self, gridLayout):
        for i in range(gridLayout.rowCount()):
            for j in range(gridLayout.columnCount()):
                if gridLayout.itemAtPosition(i, j).widget() == self.mainWindow.sender():
                    return (i, j)

        return (-1, -1)
