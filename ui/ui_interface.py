# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 727)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"    color: #fff;\n"
"    font-family: \" San Francisco\";\n"
"    font-size: 12px;\n"
"    border: nine;\n"
"    background: none;\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-color: rgba(33, 43, 51);\n"
"}\n"
"\n"
"#left_menu_widget, #csv_content, #graph_representation, #network_overview, #edge_overview, #node_overview, #upload_csv {\n"
"    background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"\n"
"#header_frame, #frame_3, frame_5 {\n"
"    background-color: rgb(61, 80, 95);\n"
"}\n"
"\n"
"#header_nav QPushButton {\n"
"    background-color: rgba(61, 80, 95);\n"
"    border-radius: 15px;\n"
"    border: 9px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"#header_nav QPushButton:hover {\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"\n"
"#frame_4 QPushButton {\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu_widget = QtWidgets.QFrame(self.centralwidget)
        self.left_menu_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_widget.setObjectName("left_menu_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setMinimumSize(QtCore.QSize(50, 50))
        self.label_14.setMaximumSize(QtCore.QSize(50, 50))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("gui\\icons/logo.svg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui\\icons/csv_content.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui\\icons/graph.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("gui\\icons/network.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("gui\\icons/edges.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("gui\\icons/node.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("gui\\icons/upload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.left_menu_widget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.left_menu_widget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_frame = QtWidgets.QFrame(self.frame_2)
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.header_frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_6.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("gui\\icons/menu-main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_3.addWidget(self.frame_10, 0, QtCore.Qt.AlignLeft)
        self.frame_11 = QtWidgets.QFrame(self.header_frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.header_nav = QtWidgets.QFrame(self.header_frame)
        self.header_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_nav.setObjectName("header_nav")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_nav)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.header_nav)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("gui\\icons/reduce.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_8 = QtWidgets.QPushButton(self.header_nav)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("gui\\icons/extend.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.header_nav)
        self.pushButton_7.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("gui\\icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon9)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.horizontalLayout_3.addWidget(self.header_nav, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_7)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.graph_representation = QtWidgets.QWidget()
        self.graph_representation.setObjectName("graph_representation")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.graph_representation)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_15 = QtWidgets.QFrame(self.graph_representation)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_9.addWidget(self.frame_15, 0, QtCore.Qt.AlignTop)
        self.frame_16 = QtWidgets.QFrame(self.graph_representation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_9.addWidget(self.frame_16)
        self.stackedWidget.addWidget(self.graph_representation)
        self.network_overview = QtWidgets.QWidget()
        self.network_overview.setObjectName("network_overview")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.network_overview)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_20 = QtWidgets.QFrame(self.network_overview)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_11.addWidget(self.frame_20)
        self.frame_19 = QtWidgets.QFrame(self.network_overview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_11.addWidget(self.frame_19)
        self.stackedWidget.addWidget(self.network_overview)
        self.edge_overview = QtWidgets.QWidget()
        self.edge_overview.setObjectName("edge_overview")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.edge_overview)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_22 = QtWidgets.QFrame(self.edge_overview)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_12.addWidget(self.frame_22)
        self.frame_21 = QtWidgets.QFrame(self.edge_overview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_12.addWidget(self.frame_21)
        self.stackedWidget.addWidget(self.edge_overview)
        self.node_overview = QtWidgets.QWidget()
        self.node_overview.setObjectName("node_overview")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.node_overview)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_24 = QtWidgets.QFrame(self.node_overview)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_13.addWidget(self.frame_24)
        self.frame_23 = QtWidgets.QFrame(self.node_overview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_23)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_13.addWidget(self.frame_23)
        self.stackedWidget.addWidget(self.node_overview)
        self.csv_content = QtWidgets.QWidget()
        self.csv_content.setObjectName("csv_content")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.csv_content)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_18 = QtWidgets.QFrame(self.csv_content)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.frame_18.setFont(font)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily(" San Francisco")
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_18)
        self.frame_17 = QtWidgets.QFrame(self.csv_content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_10.addWidget(self.frame_17)
        self.stackedWidget.addWidget(self.csv_content)
        self.verticalLayout_8.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_6.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_8)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.size_grip = QtWidgets.QFrame(self.frame_14)
        self.size_grip.setGeometry(QtCore.QRect(60, 40, 120, 80))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_6.addWidget(self.frame_14)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "InfoVis"))
        self.pushButton_10.setText(_translate("MainWindow", "CSV Content"))
        self.pushButton_3.setText(_translate("MainWindow", "Graph Representation"))
        self.pushButton_5.setText(_translate("MainWindow", "Network Overview"))
        self.pushButton_4.setText(_translate("MainWindow", "Edge Overview"))
        self.pushButton_2.setText(_translate("MainWindow", "Node Overview"))
        self.pushButton_9.setText(_translate("MainWindow", "Upload CSV"))
        self.label_2.setText(_translate("MainWindow", "Network Layout"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "MENU"))
        self.label_7.setText(_translate("MainWindow", "DASHBOARD"))
        self.label_9.setText(_translate("MainWindow", "Graph Representation"))
        self.label_11.setText(_translate("MainWindow", "Network Overview"))
        self.label_12.setText(_translate("MainWindow", "Edge Overview"))
        self.label_13.setText(_translate("MainWindow", "Node Overview"))
        self.label_10.setText(_translate("MainWindow", "CSV Content"))
        self.label_8.setText(_translate("MainWindow", "Project for Information Visualization course"))
