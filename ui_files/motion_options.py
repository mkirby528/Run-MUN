# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motion_options.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(1081, 123)
        root.setMaximumSize(QtCore.QSize(16777215, 123))
        root.setStyleSheet("#root{\n"
"    background-color: #99badd;\n"
"\n"
"}\n"
"\n"
"#delegate_label, \n"
"#duration_label,\n"
"#speaking_time_label,\n"
"#topic_label,\n"
"#first_or_last_label{\n"
"    color:white;\n"
"    font: 87 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#mod_check_box,\n"
"#unmod_check_box,\n"
"#other_check_box{\n"
"\n"
"    color:white;\n"
"    font: 87 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#delegates_combo_box{\n"
"    background-color: #767676;\n"
"    color:white;\n"
"\n"
"    font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"#first_check_box, #last_check_box{\n"
"\n"
"    color:white;\n"
"    font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"#start_motion_button{\n"
"    background-color: transparent\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(root)
        self.gridLayout.setObjectName("gridLayout")
        self.other_check_box = QtWidgets.QCheckBox(root)
        self.other_check_box.setAutoExclusive(True)
        self.other_check_box.setObjectName("other_check_box")
        self.gridLayout.addWidget(self.other_check_box, 4, 1, 1, 1)
        self.delegate_label = QtWidgets.QLabel(root)
        self.delegate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.delegate_label.setObjectName("delegate_label")
        self.gridLayout.addWidget(self.delegate_label, 1, 0, 1, 1)
        self.duration_label = QtWidgets.QLabel(root)
        self.duration_label.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_label.setObjectName("duration_label")
        self.gridLayout.addWidget(self.duration_label, 1, 2, 1, 1)
        self.unmod_check_box = QtWidgets.QCheckBox(root)
        self.unmod_check_box.setAutoExclusive(True)
        self.unmod_check_box.setObjectName("unmod_check_box")
        self.gridLayout.addWidget(self.unmod_check_box, 3, 1, 1, 1)
        self.mod_check_box = QtWidgets.QCheckBox(root)
        self.mod_check_box.setAutoExclusive(True)
        self.mod_check_box.setObjectName("mod_check_box")
        self.gridLayout.addWidget(self.mod_check_box, 1, 1, 1, 1)
        self.topic_label = QtWidgets.QLabel(root)
        self.topic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.topic_label.setObjectName("topic_label")
        self.gridLayout.addWidget(self.topic_label, 1, 4, 1, 1)
        self.speaking_time_label = QtWidgets.QLabel(root)
        self.speaking_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speaking_time_label.setObjectName("speaking_time_label")
        self.gridLayout.addWidget(self.speaking_time_label, 1, 3, 1, 1)
        self.delegates_combo_box = QtWidgets.QComboBox(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.delegates_combo_box.sizePolicy().hasHeightForWidth())
        self.delegates_combo_box.setSizePolicy(sizePolicy)
        self.delegates_combo_box.setMaximumSize(QtCore.QSize(16777215, 30))
        self.delegates_combo_box.setCurrentText("")
        self.delegates_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.delegates_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.delegates_combo_box.setFrame(True)
        self.delegates_combo_box.setObjectName("delegates_combo_box")
        self.gridLayout.addWidget(self.delegates_combo_box, 3, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(root)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(root)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 4, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(root)
        self.spinBox.setMinimum(1)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 3, 1, 1)
        self.first_or_last_label = QtWidgets.QLabel(root)
        self.first_or_last_label.setObjectName("first_or_last_label")
        self.gridLayout.addWidget(self.first_or_last_label, 1, 5, 1, 1)
        self.first_check_box = QtWidgets.QCheckBox(root)
        self.first_check_box.setAutoExclusive(True)
        self.first_check_box.setObjectName("first_check_box")
        self.gridLayout.addWidget(self.first_check_box, 3, 5, 1, 1)
        self.last_check_box = QtWidgets.QCheckBox(root)
        self.last_check_box.setAutoExclusive(True)
        self.last_check_box.setObjectName("last_check_box")
        self.gridLayout.addWidget(self.last_check_box, 4, 5, 1, 1)
        self.start_motion_button = QtWidgets.QPushButton(root)
        self.start_motion_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_motion_button.setIcon(icon)
        self.start_motion_button.setIconSize(QtCore.QSize(50, 32))
        self.start_motion_button.setObjectName("start_motion_button")
        self.gridLayout.addWidget(self.start_motion_button, 3, 6, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Form"))
        self.other_check_box.setText(_translate("root", "Other"))
        self.delegate_label.setText(_translate("root", "Delegate"))
        self.duration_label.setText(_translate("root", "Duration(Minutes)"))
        self.unmod_check_box.setText(_translate("root", "Unmod"))
        self.mod_check_box.setText(_translate("root", "Mod"))
        self.topic_label.setText(_translate("root", "Topic"))
        self.speaking_time_label.setText(_translate("root", "Speaking time(Seconds)"))
        self.first_or_last_label.setText(_translate("root", "First or Last?"))
        self.first_check_box.setText(_translate("root", "First Speech"))
        self.last_check_box.setText(_translate("root", "Last Speech"))

import res_rc
