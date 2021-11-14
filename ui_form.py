# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.resize(1291, 603)
        self.gridLayout_7 = QtWidgets.QGridLayout(MainView)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_3 = QtWidgets.QSplitter(MainView)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.cameras_box = QtWidgets.QGroupBox(self.splitter_2)
        self.cameras_box.setObjectName("cameras_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.cameras_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.camera_camboBox = QtWidgets.QComboBox(self.cameras_box)
        self.camera_camboBox.setObjectName("camera_camboBox")
        self.camera_camboBox.addItem("")
        self.camera_camboBox.addItem("")
        self.camera_camboBox.addItem("")
        self.camera_camboBox.addItem("")
        self.gridLayout_6.addWidget(self.camera_camboBox, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.record_camera = QtWidgets.QPushButton(self.cameras_box)
        self.record_camera.setObjectName("record_camera")
        self.horizontalLayout_2.addWidget(self.record_camera)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.take_picture_button = QtWidgets.QPushButton(self.cameras_box)
        self.take_picture_button.setObjectName("take_picture_button")
        self.gridLayout_6.addWidget(self.take_picture_button, 1, 2, 1, 1)
        self.funnel_cake_box = QtWidgets.QGroupBox(self.splitter_2)
        self.funnel_cake_box.setObjectName("funnel_cake_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.funnel_cake_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.funnel_cake_box)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.water_pump_button = QtWidgets.QPushButton(self.widget)
        self.water_pump_button.setObjectName("water_pump_button")
        self.verticalLayout_3.addWidget(self.water_pump_button)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.run_pump_button = QtWidgets.QPushButton(self.widget)
        self.run_pump_button.setObjectName("run_pump_button")
        self.horizontalLayout_3.addWidget(self.run_pump_button)
        self.pump_number = QtWidgets.QLabel(self.widget)
        self.pump_number.setObjectName("pump_number")
        self.horizontalLayout_3.addWidget(self.pump_number)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.pumps_dial = QtWidgets.QDial(self.splitter)
        self.pumps_dial.setMinimum(1)
        self.pumps_dial.setMaximum(6)
        self.pumps_dial.setSingleStep(1)
        self.pumps_dial.setWrapping(True)
        self.pumps_dial.setNotchesVisible(True)
        self.pumps_dial.setObjectName("pumps_dial")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.splitter_3)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.platform_box = QtWidgets.QGroupBox(self.widget1)
        self.platform_box.setObjectName("platform_box")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.platform_box)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.platform_box)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.platform_slider = QtWidgets.QSlider(self.platform_box)
        self.platform_slider.setMaximum(10)
        self.platform_slider.setOrientation(QtCore.Qt.Horizontal)
        self.platform_slider.setObjectName("platform_slider")
        self.horizontalLayout.addWidget(self.platform_slider)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.flashlight_button = QtWidgets.QPushButton(self.platform_box)
        self.flashlight_button.setObjectName("flashlight_button")
        self.gridLayout_4.addWidget(self.flashlight_button, 1, 0, 1, 1)
        self.brush_button = QtWidgets.QPushButton(self.platform_box)
        self.brush_button.setObjectName("brush_button")
        self.gridLayout_4.addWidget(self.brush_button, 0, 0, 1, 1)
        self.uv_camera_button = QtWidgets.QPushButton(self.platform_box)
        self.uv_camera_button.setObjectName("uv_camera_button")
        self.gridLayout_4.addWidget(self.uv_camera_button, 1, 1, 1, 1)
        self.microscope_button = QtWidgets.QPushButton(self.platform_box)
        self.microscope_button.setObjectName("microscope_button")
        self.gridLayout_4.addWidget(self.microscope_button, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.platform_box)
        self.sample_box = QtWidgets.QGroupBox(self.widget1)
        self.sample_box.setObjectName("sample_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.sample_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.collect_sample_button = QtWidgets.QPushButton(self.sample_box)
        self.collect_sample_button.setObjectName("collect_sample_button")
        self.gridLayout_3.addWidget(self.collect_sample_button, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.sample_box)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.sample_box)
        self.horizontalLayout_4.addWidget(self.splitter_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(MainView)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(MainView)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 1, 0, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(MainView)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 1, 1, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(MainView)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 0, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        _translate = QtCore.QCoreApplication.translate
        MainView.setWindowTitle(_translate("MainView", "MainView"))
        self.cameras_box.setTitle(_translate("MainView", "Camera View"))
        self.camera_camboBox.setItemText(0, _translate("MainView", "Camera 1"))
        self.camera_camboBox.setItemText(1, _translate("MainView", "Camera 2"))
        self.camera_camboBox.setItemText(2, _translate("MainView", "Camera 3"))
        self.camera_camboBox.setItemText(3, _translate("MainView", "Camera 4"))
        self.record_camera.setText(_translate("MainView", "Record"))
        self.take_picture_button.setText(_translate("MainView", "Take Picture"))
        self.funnel_cake_box.setTitle(_translate("MainView", "Funnel Cake"))
        self.water_pump_button.setText(_translate("MainView", "Water Pump"))
        self.run_pump_button.setText(_translate("MainView", "Run Pump:"))
        self.pump_number.setText(_translate("MainView", "1"))
        self.platform_box.setTitle(_translate("MainView", "Platform"))
        self.label.setText(_translate("MainView", "Platform Height"))
        self.flashlight_button.setText(_translate("MainView", "Flashlight"))
        self.brush_button.setText(_translate("MainView", "Brush"))
        self.uv_camera_button.setText(_translate("MainView", "UV Camera"))
        self.microscope_button.setText(_translate("MainView", "Microscope"))
        self.sample_box.setTitle(_translate("MainView", "Sample"))
        self.collect_sample_button.setText(_translate("MainView", "Collect Sample"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainView = QtWidgets.QWidget()
    ui = Ui_MainView()
    ui.setupUi(MainView)
    MainView.show()
    sys.exit(app.exec_())