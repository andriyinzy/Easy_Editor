# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Easy_Editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1302, 827)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 690, 1661, 236))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenFolder = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.OpenFolder.setStyleSheet("\n"
"  align-items: center;\n"
"  background-clip: padding-box;\n"
"  background-color: #fa6400;\n"
"  border: 1px solid transparent;\n"
"  border-radius: .25rem;\n"
"  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  display: inline-flex;\n"
"  font-family: system-ui,-apple-system,system-ui,\"Helvetica Neue\",Helvetica,Arial,sans-serif;\n"
"  font-size: 12px;\n"
"  font-weight: 600;\n"
"  justify-content: center;\n"
"  line-height: 1.25;\n"
"  margin: 0;\n"
"  min-height: 3rem;\n"
"  padding: calc(.875rem - 1px) calc(1.5rem - 1px);\n"
"  position: relative;\n"
"  text-decoration: none;\n"
"  transition: all 250ms;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: baseline;\n"
"  width: auto;\n"
"")
        self.OpenFolder.setObjectName("OpenFolder")
        self.verticalLayout.addWidget(self.OpenFolder)
        self.listView = QtWidgets.QListView(self.horizontalLayoutWidget_3)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_14.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_13.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_12.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_11.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_10.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_9.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_8.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_7.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_6.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setStyleSheet("\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -50, 1601, 731))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenFolder.setText(_translate("MainWindow", "Open Folder"))
        self.pushButton_14.setText(_translate("MainWindow", "Contour"))
        self.pushButton_13.setText(_translate("MainWindow", "Emboss"))
        self.pushButton_12.setText(_translate("MainWindow", "E_E"))
        self.pushButton_11.setText(_translate("MainWindow", "Detail"))
        self.pushButton_10.setText(_translate("MainWindow", "F_E"))
        self.pushButton_2.setText(_translate("MainWindow", "Smooth"))
        self.pushButton_4.setText(_translate("MainWindow", "Left"))
        self.pushButton_9.setText(_translate("MainWindow", "Right"))
        self.pushButton_8.setText(_translate("MainWindow", "Sharp"))
        self.pushButton_7.setText(_translate("MainWindow", "B/W"))
        self.pushButton_6.setText(_translate("MainWindow", "Flip"))
        self.pushButton_5.setText(_translate("MainWindow", "U/D"))
        self.pushButton_3.setText(_translate("MainWindow", "Blur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
