# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speaker_view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(400, 121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())
        root.setSizePolicy(sizePolicy)
        root.setStyleSheet("#root, #StackedWidget, #display_mode_view, #add_mode_view{\n"
"    background-color: #13294B;\n"
"\n"
"}\n"
"\n"
"\n"
"#speaker_name_label,#speaker_number_label{\n"
"    color:white;\n"
"    font: 24pt \"MS UI Gothic\";\n"
"    text-decoration: underline;\n"
"\n"
"}\n"
"\n"
"#confirm_speaker_button, #add_speaker_button,#cancel_speaker_button{\n"
"        background-color: transparent;    \n"
"}\n"
"\n"
"#add_speaker_combo_box{\n"
"    color:white;\n"
"    background-color: #767676;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";    \n"
"    border-style: ridge;\n"
"    border-width: 0px,5px,0px,0px;\n"
"    border-color: #777777;\n"
"    padding: 5px\n"
"}\n"
"")
        self.display_mode_view = QtWidgets.QWidget()
        self.display_mode_view.setObjectName("display_mode_view")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.display_mode_view)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.speaker_number_label = QtWidgets.QLabel(self.display_mode_view)
        self.speaker_number_label.setStyleSheet("background-color:#13294B")
        self.speaker_number_label.setObjectName("speaker_number_label")
        self.horizontalLayout.addWidget(self.speaker_number_label)
        self.speaker_name_label = QtWidgets.QLabel(self.display_mode_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speaker_name_label.sizePolicy().hasHeightForWidth())
        self.speaker_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.speaker_name_label.setFont(font)
        self.speaker_name_label.setStyleSheet("background-color: #13294B")
        self.speaker_name_label.setText("")
        self.speaker_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speaker_name_label.setObjectName("speaker_name_label")
        self.horizontalLayout.addWidget(self.speaker_name_label)
        self.add_speaker_button = QtWidgets.QPushButton(self.display_mode_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_speaker_button.sizePolicy().hasHeightForWidth())
        self.add_speaker_button.setSizePolicy(sizePolicy)
        self.add_speaker_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_speaker_button.setIcon(icon)
        self.add_speaker_button.setIconSize(QtCore.QSize(32, 32))
        self.add_speaker_button.setObjectName("add_speaker_button")
        self.horizontalLayout.addWidget(self.add_speaker_button)
        root.addWidget(self.display_mode_view)
        self.add_mode_view = QtWidgets.QWidget()
        self.add_mode_view.setObjectName("add_mode_view")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.add_mode_view)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_speaker_combo_box = QtWidgets.QComboBox(self.add_mode_view)
        self.add_speaker_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.add_speaker_combo_box.setDuplicatesEnabled(False)
        self.add_speaker_combo_box.setObjectName("add_speaker_combo_box")
        self.horizontalLayout_2.addWidget(self.add_speaker_combo_box)
        self.cancel_speaker_button = QtWidgets.QPushButton(self.add_mode_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_speaker_button.sizePolicy().hasHeightForWidth())
        self.cancel_speaker_button.setSizePolicy(sizePolicy)
        self.cancel_speaker_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/cancel_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_speaker_button.setIcon(icon1)
        self.cancel_speaker_button.setIconSize(QtCore.QSize(32, 32))
        self.cancel_speaker_button.setObjectName("cancel_speaker_button")
        self.horizontalLayout_2.addWidget(self.cancel_speaker_button)
        self.confirm_speaker_button = QtWidgets.QPushButton(self.add_mode_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_speaker_button.sizePolicy().hasHeightForWidth())
        self.confirm_speaker_button.setSizePolicy(sizePolicy)
        self.confirm_speaker_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/check_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm_speaker_button.setIcon(icon2)
        self.confirm_speaker_button.setIconSize(QtCore.QSize(32, 32))
        self.confirm_speaker_button.setObjectName("confirm_speaker_button")
        self.horizontalLayout_2.addWidget(self.confirm_speaker_button)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        root.addWidget(self.add_mode_view)

        self.retranslateUi(root)
        root.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "StackedWidget"))
        self.speaker_number_label.setText(_translate("root", "1"))

import res_rc
