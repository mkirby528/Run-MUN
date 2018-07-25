# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delegate_view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(800, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())
        root.setSizePolicy(sizePolicy)
        root.setWindowTitle("")
        root.setStyleSheet("#root{\n"
"    background-color: #4B9CD3;\n"
"\n"
"}\n"
"\n"
"#delegate_name_label{\n"
"    color:white;\n"
"    \n"
"    font: 24pt \"Poor Richard\";\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"#delete_delegate_button{\n"
"        background-color: transparent;    \n"
"}\n"
"\n"
"#present_button:checked, #absent_button:checked{\n"
"    background-color: #13294B;\n"
"    border:none;\n"
"    color:white;\n"
"    font: 87 16pt \"Arial Black\";\n"
"}\n"
"\n"
"#present_button, #absent_button{\n"
"    background-color: #767676;\n"
"    border:none;\n"
"    color:white;\n"
"    font: 87 16pt \"Arial Black\";\n"
"}")
        root.setProperty("index", 0)
        self.horizontalLayout = QtWidgets.QHBoxLayout(root)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delegate_name_label = QtWidgets.QLabel(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delegate_name_label.sizePolicy().hasHeightForWidth())
        self.delegate_name_label.setSizePolicy(sizePolicy)
        self.delegate_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.delegate_name_label.setObjectName("delegate_name_label")
        self.horizontalLayout.addWidget(self.delegate_name_label)
        self.present_button = QtWidgets.QPushButton(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.present_button.sizePolicy().hasHeightForWidth())
        self.present_button.setSizePolicy(sizePolicy)
        self.present_button.setStyleSheet("")
        self.present_button.setCheckable(True)
        self.present_button.setChecked(True)
        self.present_button.setAutoExclusive(True)
        self.present_button.setObjectName("present_button")
        self.horizontalLayout.addWidget(self.present_button)
        self.absent_button = QtWidgets.QPushButton(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absent_button.sizePolicy().hasHeightForWidth())
        self.absent_button.setSizePolicy(sizePolicy)
        self.absent_button.setCheckable(True)
        self.absent_button.setChecked(False)
        self.absent_button.setAutoExclusive(True)
        self.absent_button.setFlat(False)
        self.absent_button.setObjectName("absent_button")
        self.horizontalLayout.addWidget(self.absent_button)
        self.delete_delegate_button = QtWidgets.QPushButton(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_delegate_button.sizePolicy().hasHeightForWidth())
        self.delete_delegate_button.setSizePolicy(sizePolicy)
        self.delete_delegate_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_delegate_button.setIcon(icon)
        self.delete_delegate_button.setIconSize(QtCore.QSize(32, 32))
        self.delete_delegate_button.setObjectName("delete_delegate_button")
        self.horizontalLayout.addWidget(self.delete_delegate_button)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        self.delegate_name_label.setText(_translate("root", "Delegate Name"))
        self.present_button.setText(_translate("root", "Present "))
        self.present_button.setProperty("but_name", _translate("root", "fafafa"))
        self.absent_button.setText(_translate("root", "Absent"))

import res_rc
