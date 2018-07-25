# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mun_app_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(1197, 794)
        font = QtGui.QFont()
        font.setPointSize(18)
        root.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/gavel-icon-18659-Windows.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        root.setWindowIcon(icon)
        root.setStyleSheet("QFrame#sidebar{\n"
"    background-color: #13294B;\n"
"}\n"
"\n"
"QLabel#app_title{\n"
"    color:white;\n"
"    font: 75 24pt \"Poor Richard\";\n"
"}\n"
"#home_button,#delegates_button,#points_motions_button,#settings_button, #moderated_caucus_button {\n"
"        background-color: transparent;\n"
"        border-color: transparent;\n"
"        color:white;    \n"
"        width: 100%;\n"
"        margin: 0px;        \n"
"        height: 50px\n"
"}\n"
"\n"
"QPushButton#home_button:hover,#delegates_button:hover,#points_motions_button:hover,#settings_button:hover,#moderated_caucus_button:hover{\n"
"    background-color: #4B9CD3;\n"
"\n"
"}\n"
"\n"
"#settings_page, #points_motions_page, #moderated_caucus_page{\n"
"    background-color: #4B9CD3;\n"
"\n"
"}\n"
"\n"
"#settings_title_label, #delegates_title_label, #points_and_motions_label,#moderated_caucus_title_label{\n"
"    color:white;\n"
"    font: 24pt \"Arial Black\";\n"
"    padding-bottom: 10px;\n"
"\n"
"}\n"
"\n"
"#conference_title_label,#committee_title_label,#chair_label, #co_chair_label,#cd_label{\n"
"    color:white;\n"
"    font: 16pt \"Arial Black\";\n"
"}\n"
"\n"
"#conference_title_field,#committee_title_field, #chair_field,#co_chair_field,#cd_field{\n"
"    color:white;\n"
"    background-color: #4B9CD3;\n"
"    font: 12pt \"Arial Black\";\n"
"    border-style: ridge;\n"
"    border-width: 0px,5px,0px,0px;\n"
"    border-color: #13294B;\n"
"    padding: 5px\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color:                  white;\n"
"    font: 14pt \"Arial Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          25%;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       #13294B;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"#save_button{\n"
"    background-color: #13294b;\n"
"    color: white;\n"
"    font: 30pt \"Wide Latin\";\n"
"}\n"
"\n"
"#delegates_page, #dels_scroll_area{\n"
"        background-color: #4B9CD3;\n"
"}\n"
"\n"
"#add_delegate_button, #add_motion_button, #add_mod_caucus_button{\n"
"    background-color: #767676;\n"
"    border-color: transparent;\n"
"    color:white;\n"
"    font: 20pt \"Poor Richard\";\n"
"}\n"
"\n"
"#dels_layout, #dels_scroll_area{\n"
"    background-color: \"#4B9CD3\";\n"
"    border-color: transparent\n"
"}\n"
"\n"
"#points_motion_scroll_contents {\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"#delegates_info_label, #mod_info_label,#mod_speakers_list_label{\n"
"    background-color:#13294B;\n"
"    color:white;\n"
"    font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"#add_delegate_page, #add_mod_caucus_page{\n"
"background-color: #767676;\n"
"}\n"
"#add_delegate_page_title, #add_mod_caucus_title{\n"
"    color:white;\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#add_delegate_name_field, #add_mod_topic_field{\n"
"    color:white;\n"
"    background-color: #767676;\n"
"    font: 75 24pt \"MS Shell Dlg 2\";    border-style: ridge;\n"
"    border-width: 0px,5px,0px,0px;\n"
"    border-color: #777777;\n"
"    padding: 5px\n"
"}\n"
"\n"
"#cancel_button, #cancel_button_mod{\n"
"    background-color: red;\n"
"    color: black;\n"
"    font: 87 24pt \"Arial Black\";\n"
"}\n"
"\n"
"\n"
"#confirm_add_button, #confirm_add_button_mod{\n"
"    background-color: lime;\n"
"    color: black;\n"
"    font: 87 24pt \"Arial Black\";\n"
"}\n"
"\n"
"#duration_spin_box, #speaking_time_spin_box, #motioned_by_combo_box{\n"
"    color:white;\n"
"    background-color: #767676;\n"
"    font: 75 14pt \"MS Shell Dlg 2\";    \n"
"    border-style: ridge;\n"
"    border-width: 0px,5px,0px,0px;\n"
"    border-color: #777777;\n"
"    padding: 5px\n"
"}\n"
"\n"
"\n"
"#add_topic_label, #add_duration_label, #add_speaking_time_label, #motioned_by_label, #first_or_last_label{\n"
"    color:white;\n"
"    font: 87 14pt \"Arial Black\";\n"
"}\n"
"\n"
"#first_speech_button:checked, #last_speech_button:checked{\n"
"    background-color: #13294B;\n"
"    border:none;\n"
"    color:white;\n"
"    font: 87 16pt \"Arial Black\";\n"
"}\n"
"\n"
"#first_speech_button, #last_speech_button{\n"
"    background-color: #767676;\n"
"    border:none;\n"
"    color:white;\n"
"    font: 87 16pt \"Arial Black\";\n"
"}\n"
"\n"
"")
        self.gridLayout_4 = QtWidgets.QGridLayout(root)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.content_pane = QtWidgets.QStackedWidget(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_pane.sizePolicy().hasHeightForWidth())
        self.content_pane.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.content_pane.setFont(font)
        self.content_pane.setFrameShape(QtWidgets.QFrame.HLine)
        self.content_pane.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.content_pane.setLineWidth(0)
        self.content_pane.setObjectName("content_pane")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.content_pane.addWidget(self.home_page)
        self.delegates_page = QtWidgets.QWidget()
        self.delegates_page.setObjectName("delegates_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.delegates_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.delegates_title_label = QtWidgets.QLabel(self.delegates_page)
        self.delegates_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.delegates_title_label.setObjectName("delegates_title_label")
        self.verticalLayout.addWidget(self.delegates_title_label)
        self.delegates_info_label = QtWidgets.QLabel(self.delegates_page)
        self.delegates_info_label.setText("")
        self.delegates_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.delegates_info_label.setObjectName("delegates_info_label")
        self.verticalLayout.addWidget(self.delegates_info_label)
        self.add_delegate_button = QtWidgets.QPushButton(self.delegates_page)
        self.add_delegate_button.setObjectName("add_delegate_button")
        self.verticalLayout.addWidget(self.add_delegate_button)
        self.delegates_scroll_area = QtWidgets.QScrollArea(self.delegates_page)
        self.delegates_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.delegates_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.delegates_scroll_area.setLineWidth(0)
        self.delegates_scroll_area.setWidgetResizable(True)
        self.delegates_scroll_area.setObjectName("delegates_scroll_area")
        self.dels_scroll_area = QtWidgets.QWidget()
        self.dels_scroll_area.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.dels_scroll_area.setObjectName("dels_scroll_area")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dels_scroll_area)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dels_layout = QtWidgets.QVBoxLayout()
        self.dels_layout.setSpacing(10)
        self.dels_layout.setObjectName("dels_layout")
        self.verticalLayout_3.addLayout(self.dels_layout)
        self.delegates_scroll_area.setWidget(self.dels_scroll_area)
        self.verticalLayout.addWidget(self.delegates_scroll_area)
        self.content_pane.addWidget(self.delegates_page)
        self.add_delegate_page = QtWidgets.QWidget()
        self.add_delegate_page.setStyleSheet("")
        self.add_delegate_page.setObjectName("add_delegate_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.add_delegate_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_delegate_page_title = QtWidgets.QLabel(self.add_delegate_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_delegate_page_title.sizePolicy().hasHeightForWidth())
        self.add_delegate_page_title.setSizePolicy(sizePolicy)
        self.add_delegate_page_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.add_delegate_page_title.setObjectName("add_delegate_page_title")
        self.verticalLayout_2.addWidget(self.add_delegate_page_title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.add_delegate_name_field = QtWidgets.QLineEdit(self.add_delegate_page)
        self.add_delegate_name_field.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.add_delegate_name_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.add_delegate_name_field.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.add_delegate_name_field.setPlaceholderText("")
        self.add_delegate_name_field.setClearButtonEnabled(True)
        self.add_delegate_name_field.setObjectName("add_delegate_name_field")
        self.verticalLayout_2.addWidget(self.add_delegate_name_field)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(self.add_delegate_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMaximumSize(QtCore.QSize(16777215, 100))
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout_2.addWidget(self.cancel_button)
        self.confirm_add_button = QtWidgets.QPushButton(self.add_delegate_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_add_button.sizePolicy().hasHeightForWidth())
        self.confirm_add_button.setSizePolicy(sizePolicy)
        self.confirm_add_button.setMaximumSize(QtCore.QSize(16777215, 100))
        self.confirm_add_button.setObjectName("confirm_add_button")
        self.verticalLayout_2.addWidget(self.confirm_add_button)
        self.content_pane.addWidget(self.add_delegate_page)
        self.points_motions_page = QtWidgets.QWidget()
        self.points_motions_page.setObjectName("points_motions_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.points_motions_page)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.points_and_motions_label = QtWidgets.QLabel(self.points_motions_page)
        self.points_and_motions_label.setAlignment(QtCore.Qt.AlignCenter)
        self.points_and_motions_label.setObjectName("points_and_motions_label")
        self.verticalLayout_4.addWidget(self.points_and_motions_label)
        self.add_motion_button = QtWidgets.QPushButton(self.points_motions_page)
        self.add_motion_button.setObjectName("add_motion_button")
        self.verticalLayout_4.addWidget(self.add_motion_button)
        self.points_motions_scroll_area = QtWidgets.QScrollArea(self.points_motions_page)
        self.points_motions_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.points_motions_scroll_area.setWidgetResizable(True)
        self.points_motions_scroll_area.setObjectName("points_motions_scroll_area")
        self.points_motion_scroll_contents = QtWidgets.QWidget()
        self.points_motion_scroll_contents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.points_motion_scroll_contents.setObjectName("points_motion_scroll_contents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.points_motion_scroll_contents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.points_motions_layout = QtWidgets.QVBoxLayout()
        self.points_motions_layout.setSpacing(20)
        self.points_motions_layout.setObjectName("points_motions_layout")
        self.verticalLayout_7.addLayout(self.points_motions_layout)
        self.points_motions_scroll_area.setWidget(self.points_motion_scroll_contents)
        self.verticalLayout_4.addWidget(self.points_motions_scroll_area)
        self.content_pane.addWidget(self.points_motions_page)
        self.moderated_caucus_page = QtWidgets.QWidget()
        self.moderated_caucus_page.setObjectName("moderated_caucus_page")
        self.gridLayout = QtWidgets.QGridLayout(self.moderated_caucus_page)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.mod_timer_button_bar = QtWidgets.QFrame(self.moderated_caucus_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mod_timer_button_bar.sizePolicy().hasHeightForWidth())
        self.mod_timer_button_bar.setSizePolicy(sizePolicy)
        self.mod_timer_button_bar.setObjectName("mod_timer_button_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mod_timer_button_bar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_timer_mod = QtWidgets.QPushButton(self.mod_timer_button_bar)
        self.start_timer_mod.setObjectName("start_timer_mod")
        self.horizontalLayout.addWidget(self.start_timer_mod)
        self.pause_timer_mod = QtWidgets.QPushButton(self.mod_timer_button_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.pause_timer_mod.sizePolicy().hasHeightForWidth())
        self.pause_timer_mod.setSizePolicy(sizePolicy)
        self.pause_timer_mod.setObjectName("pause_timer_mod")
        self.horizontalLayout.addWidget(self.pause_timer_mod)
        self.reset_timer_mod = QtWidgets.QPushButton(self.mod_timer_button_bar)
        self.reset_timer_mod.setObjectName("reset_timer_mod")
        self.horizontalLayout.addWidget(self.reset_timer_mod)
        self.gridLayout.addWidget(self.mod_timer_button_bar, 4, 0, 1, 1)
        self.mod_speakers_list_label = QtWidgets.QLabel(self.moderated_caucus_page)
        self.mod_speakers_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mod_speakers_list_label.setObjectName("mod_speakers_list_label")
        self.gridLayout.addWidget(self.mod_speakers_list_label, 2, 1, 1, 1)
        self.mod_info_label = QtWidgets.QLabel(self.moderated_caucus_page)
        self.mod_info_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mod_info_label.setObjectName("mod_info_label")
        self.gridLayout.addWidget(self.mod_info_label, 2, 0, 1, 1)
        self.moderated_caucus_title_label = QtWidgets.QLabel(self.moderated_caucus_page)
        self.moderated_caucus_title_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.moderated_caucus_title_label.setObjectName("moderated_caucus_title_label")
        self.gridLayout.addWidget(self.moderated_caucus_title_label, 0, 0, 1, 2)
        self.add_mod_caucus_button = QtWidgets.QPushButton(self.moderated_caucus_page)
        self.add_mod_caucus_button.setObjectName("add_mod_caucus_button")
        self.gridLayout.addWidget(self.add_mod_caucus_button, 1, 0, 1, 2)
        self.countdown_timer = QtWidgets.QLCDNumber(self.moderated_caucus_page)
        self.countdown_timer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.countdown_timer.setDigitCount(1)
        self.countdown_timer.setObjectName("countdown_timer")
        self.gridLayout.addWidget(self.countdown_timer, 3, 0, 1, 1)
        self.mod_speaker_list = QtWidgets.QScrollArea(self.moderated_caucus_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mod_speaker_list.sizePolicy().hasHeightForWidth())
        self.mod_speaker_list.setSizePolicy(sizePolicy)
        self.mod_speaker_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mod_speaker_list.setWidgetResizable(True)
        self.mod_speaker_list.setObjectName("mod_speaker_list")
        self.speaker_list_contents = QtWidgets.QWidget()
        self.speaker_list_contents.setGeometry(QtCore.QRect(0, 0, 98, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.speaker_list_contents.sizePolicy().hasHeightForWidth())
        self.speaker_list_contents.setSizePolicy(sizePolicy)
        self.speaker_list_contents.setStyleSheet("background-color: #767676;")
        self.speaker_list_contents.setObjectName("speaker_list_contents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.speaker_list_contents)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.speaker_list_layout = QtWidgets.QVBoxLayout()
        self.speaker_list_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.speaker_list_layout.setSpacing(0)
        self.speaker_list_layout.setObjectName("speaker_list_layout")
        self.verticalLayout_8.addLayout(self.speaker_list_layout)
        self.mod_speaker_list.setWidget(self.speaker_list_contents)
        self.gridLayout.addWidget(self.mod_speaker_list, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.content_pane.addWidget(self.moderated_caucus_page)
        self.add_mod_caucus_page = QtWidgets.QWidget()
        self.add_mod_caucus_page.setObjectName("add_mod_caucus_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.add_mod_caucus_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_mod_page_frame = QtWidgets.QFrame(self.add_mod_caucus_page)
        self.add_mod_page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_mod_page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_mod_page_frame.setObjectName("add_mod_page_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.add_mod_page_frame)
        self.verticalLayout_6.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.add_mod_caucus_title = QtWidgets.QLabel(self.add_mod_page_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_mod_caucus_title.sizePolicy().hasHeightForWidth())
        self.add_mod_caucus_title.setSizePolicy(sizePolicy)
        self.add_mod_caucus_title.setAlignment(QtCore.Qt.AlignCenter)
        self.add_mod_caucus_title.setObjectName("add_mod_caucus_title")
        self.verticalLayout_6.addWidget(self.add_mod_caucus_title)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.frame_2 = QtWidgets.QFrame(self.add_mod_page_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setContentsMargins(80, 0, 80, 0)
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.add_speaking_time_label = QtWidgets.QLabel(self.frame_2)
        self.add_speaking_time_label.setObjectName("add_speaking_time_label")
        self.gridLayout_5.addWidget(self.add_speaking_time_label, 4, 0, 1, 1)
        self.duration_spin_box = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.duration_spin_box.setMinimum(1.0)
        self.duration_spin_box.setObjectName("duration_spin_box")
        self.gridLayout_5.addWidget(self.duration_spin_box, 1, 1, 1, 1)
        self.add_topic_label = QtWidgets.QLabel(self.frame_2)
        self.add_topic_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.add_topic_label.setObjectName("add_topic_label")
        self.gridLayout_5.addWidget(self.add_topic_label, 0, 0, 1, 1)
        self.speaking_time_spin_box = QtWidgets.QSpinBox(self.frame_2)
        self.speaking_time_spin_box.setMinimum(1)
        self.speaking_time_spin_box.setMaximum(999)
        self.speaking_time_spin_box.setProperty("value", 30)
        self.speaking_time_spin_box.setObjectName("speaking_time_spin_box")
        self.gridLayout_5.addWidget(self.speaking_time_spin_box, 4, 1, 1, 1)
        self.add_duration_label = QtWidgets.QLabel(self.frame_2)
        self.add_duration_label.setObjectName("add_duration_label")
        self.gridLayout_5.addWidget(self.add_duration_label, 1, 0, 1, 1)
        self.add_mod_topic_field = QtWidgets.QLineEdit(self.frame_2)
        self.add_mod_topic_field.setText("")
        self.add_mod_topic_field.setObjectName("add_mod_topic_field")
        self.gridLayout_5.addWidget(self.add_mod_topic_field, 0, 1, 1, 1)
        self.motioned_by_label = QtWidgets.QLabel(self.frame_2)
        self.motioned_by_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.motioned_by_label.setObjectName("motioned_by_label")
        self.gridLayout_5.addWidget(self.motioned_by_label, 6, 0, 1, 1)
        self.motioned_by_combo_box = QtWidgets.QComboBox(self.frame_2)
        self.motioned_by_combo_box.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.motioned_by_combo_box.setObjectName("motioned_by_combo_box")
        self.gridLayout_5.addWidget(self.motioned_by_combo_box, 6, 1, 1, 1)
        self.first_or_last_label = QtWidgets.QLabel(self.frame_2)
        self.first_or_last_label.setObjectName("first_or_last_label")
        self.gridLayout_5.addWidget(self.first_or_last_label, 7, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.first_speech_button = QtWidgets.QPushButton(self.frame_3)
        self.first_speech_button.setCheckable(True)
        self.first_speech_button.setChecked(True)
        self.first_speech_button.setAutoExclusive(True)
        self.first_speech_button.setObjectName("first_speech_button")
        self.horizontalLayout_2.addWidget(self.first_speech_button)
        self.last_speech_button = QtWidgets.QPushButton(self.frame_3)
        self.last_speech_button.setCheckable(True)
        self.last_speech_button.setAutoExclusive(True)
        self.last_speech_button.setFlat(False)
        self.last_speech_button.setObjectName("last_speech_button")
        self.horizontalLayout_2.addWidget(self.last_speech_button)
        self.gridLayout_5.addWidget(self.frame_3, 7, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.cancel_button_mod = QtWidgets.QPushButton(self.add_mod_page_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button_mod.sizePolicy().hasHeightForWidth())
        self.cancel_button_mod.setSizePolicy(sizePolicy)
        self.cancel_button_mod.setMaximumSize(QtCore.QSize(16777215, 100))
        self.cancel_button_mod.setObjectName("cancel_button_mod")
        self.verticalLayout_6.addWidget(self.cancel_button_mod)
        self.confirm_add_button_mod = QtWidgets.QPushButton(self.add_mod_page_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_add_button_mod.sizePolicy().hasHeightForWidth())
        self.confirm_add_button_mod.setSizePolicy(sizePolicy)
        self.confirm_add_button_mod.setMaximumSize(QtCore.QSize(16777215, 100))
        self.confirm_add_button_mod.setObjectName("confirm_add_button_mod")
        self.verticalLayout_6.addWidget(self.confirm_add_button_mod)
        self.verticalLayout_5.addWidget(self.add_mod_page_frame)
        self.content_pane.addWidget(self.add_mod_caucus_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.formLayout = QtWidgets.QFormLayout(self.settings_page)
        self.formLayout.setContentsMargins(0, -1, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.settings_title_label = QtWidgets.QLabel(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_title_label.sizePolicy().hasHeightForWidth())
        self.settings_title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.settings_title_label.setFont(font)
        self.settings_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_title_label.setObjectName("settings_title_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.settings_title_label)
        self.conference_title_label = QtWidgets.QLabel(self.settings_page)
        self.conference_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.conference_title_label.setObjectName("conference_title_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.conference_title_label)
        self.conference_title_field = QtWidgets.QLineEdit(self.settings_page)
        self.conference_title_field.setAutoFillBackground(False)
        self.conference_title_field.setText("")
        self.conference_title_field.setMaxLength(100)
        self.conference_title_field.setFrame(True)
        self.conference_title_field.setAlignment(QtCore.Qt.AlignCenter)
        self.conference_title_field.setClearButtonEnabled(False)
        self.conference_title_field.setObjectName("conference_title_field")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.conference_title_field)
        self.committee_title_label = QtWidgets.QLabel(self.settings_page)
        self.committee_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.committee_title_label.setObjectName("committee_title_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.committee_title_label)
        self.committee_title_field = QtWidgets.QLineEdit(self.settings_page)
        self.committee_title_field.setAutoFillBackground(False)
        self.committee_title_field.setText("")
        self.committee_title_field.setFrame(True)
        self.committee_title_field.setAlignment(QtCore.Qt.AlignCenter)
        self.committee_title_field.setClearButtonEnabled(False)
        self.committee_title_field.setObjectName("committee_title_field")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.committee_title_field)
        self.chair_label = QtWidgets.QLabel(self.settings_page)
        self.chair_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chair_label.setObjectName("chair_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.chair_label)
        self.chair_field = QtWidgets.QLineEdit(self.settings_page)
        self.chair_field.setAutoFillBackground(False)
        self.chair_field.setText("")
        self.chair_field.setFrame(True)
        self.chair_field.setAlignment(QtCore.Qt.AlignCenter)
        self.chair_field.setClearButtonEnabled(False)
        self.chair_field.setObjectName("chair_field")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.chair_field)
        self.co_chair_label = QtWidgets.QLabel(self.settings_page)
        self.co_chair_label.setAlignment(QtCore.Qt.AlignCenter)
        self.co_chair_label.setObjectName("co_chair_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.co_chair_label)
        self.co_chair_field = QtWidgets.QLineEdit(self.settings_page)
        self.co_chair_field.setAutoFillBackground(False)
        self.co_chair_field.setText("")
        self.co_chair_field.setFrame(True)
        self.co_chair_field.setAlignment(QtCore.Qt.AlignCenter)
        self.co_chair_field.setClearButtonEnabled(False)
        self.co_chair_field.setObjectName("co_chair_field")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.co_chair_field)
        self.save_button = QtWidgets.QPushButton(self.settings_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.save_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.frame = QtWidgets.QFrame(self.settings_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(250, -1, 250, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.crisis_button = QtWidgets.QRadioButton(self.frame)
        self.crisis_button.setChecked(True)
        self.crisis_button.setObjectName("crisis_button")
        self.gridLayout_3.addWidget(self.crisis_button, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gap_button = QtWidgets.QRadioButton(self.frame)
        self.gap_button.setObjectName("gap_button")
        self.gridLayout_3.addWidget(self.gap_button, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.ga_button = QtWidgets.QRadioButton(self.frame)
        self.ga_button.setObjectName("ga_button")
        self.gridLayout_3.addWidget(self.ga_button, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.frame)
        self.cd_label = QtWidgets.QLabel(self.settings_page)
        self.cd_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cd_label.setObjectName("cd_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.cd_label)
        self.cd_field = QtWidgets.QLineEdit(self.settings_page)
        self.cd_field.setAlignment(QtCore.Qt.AlignCenter)
        self.cd_field.setObjectName("cd_field")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.cd_field)
        self.content_pane.addWidget(self.settings_page)
        self.gridLayout_4.addWidget(self.content_pane, 0, 1, 1, 1)
        self.sidebar = QtWidgets.QFrame(root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sidebar.setFont(font)
        self.sidebar.setStyleSheet("")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebar.setObjectName("sidebar")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sidebar)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(0, -1, 0, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.app_title = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.app_title.setFont(font)
        self.app_title.setAlignment(QtCore.Qt.AlignCenter)
        self.app_title.setWordWrap(True)
        self.app_title.setObjectName("app_title")
        self.gridLayout_2.addWidget(self.app_title, 1, 0, 1, 1)
        self.delegates_button = QtWidgets.QPushButton(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delegates_button.sizePolicy().hasHeightForWidth())
        self.delegates_button.setSizePolicy(sizePolicy)
        self.delegates_button.setMinimumSize(QtCore.QSize(20, 40))
        self.delegates_button.setMaximumSize(QtCore.QSize(200, 40))
        self.delegates_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delegates_button.setFont(font)
        self.delegates_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.delegates_button.setDefault(False)
        self.delegates_button.setFlat(False)
        self.delegates_button.setObjectName("delegates_button")
        self.gridLayout_2.addWidget(self.delegates_button, 4, 0, 1, 1)
        self.settings_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.gridLayout_2.addWidget(self.settings_button, 8, 0, 1, 1)
        self.points_motions_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.points_motions_button.setFont(font)
        self.points_motions_button.setObjectName("points_motions_button")
        self.gridLayout_2.addWidget(self.points_motions_button, 6, 0, 1, 1)
        self.cira_logo = QtWidgets.QLabel(self.sidebar)
        self.cira_logo.setText("")
        self.cira_logo.setPixmap(QtGui.QPixmap(":/img/cira_logo.png"))
        self.cira_logo.setScaledContents(True)
        self.cira_logo.setObjectName("cira_logo")
        self.gridLayout_2.addWidget(self.cira_logo, 0, 0, 1, 1)
        self.home_button = QtWidgets.QPushButton(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)
        self.home_button.setMinimumSize(QtCore.QSize(20, 40))
        self.home_button.setMaximumSize(QtCore.QSize(200, 40))
        self.home_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.home_button.setFont(font)
        self.home_button.setIconSize(QtCore.QSize(16, 16))
        self.home_button.setCheckable(False)
        self.home_button.setDefault(False)
        self.home_button.setFlat(False)
        self.home_button.setObjectName("home_button")
        self.gridLayout_2.addWidget(self.home_button, 2, 0, 1, 1)
        self.moderated_caucus_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.moderated_caucus_button.setFont(font)
        self.moderated_caucus_button.setObjectName("moderated_caucus_button")
        self.gridLayout_2.addWidget(self.moderated_caucus_button, 7, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem5, 9, 0, 1, 1)
        self.gridLayout_4.addWidget(self.sidebar, 0, 0, 1, 1)

        self.retranslateUi(root)
        self.content_pane.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(root)
        root.setTabOrder(self.points_motions_button, self.settings_button)
        root.setTabOrder(self.settings_button, self.conference_title_field)
        root.setTabOrder(self.conference_title_field, self.committee_title_field)
        root.setTabOrder(self.committee_title_field, self.chair_field)
        root.setTabOrder(self.chair_field, self.co_chair_field)
        root.setTabOrder(self.co_chair_field, self.crisis_button)
        root.setTabOrder(self.crisis_button, self.ga_button)
        root.setTabOrder(self.ga_button, self.gap_button)
        root.setTabOrder(self.gap_button, self.cd_field)
        root.setTabOrder(self.cd_field, self.save_button)
        root.setTabOrder(self.save_button, self.delegates_button)
        root.setTabOrder(self.delegates_button, self.home_button)
        root.setTabOrder(self.home_button, self.moderated_caucus_button)
        root.setTabOrder(self.moderated_caucus_button, self.add_delegate_button)
        root.setTabOrder(self.add_delegate_button, self.delegates_scroll_area)
        root.setTabOrder(self.delegates_scroll_area, self.add_delegate_name_field)
        root.setTabOrder(self.add_delegate_name_field, self.cancel_button)
        root.setTabOrder(self.cancel_button, self.confirm_add_button)
        root.setTabOrder(self.confirm_add_button, self.add_motion_button)
        root.setTabOrder(self.add_motion_button, self.points_motions_scroll_area)
        root.setTabOrder(self.points_motions_scroll_area, self.start_timer_mod)
        root.setTabOrder(self.start_timer_mod, self.pause_timer_mod)
        root.setTabOrder(self.pause_timer_mod, self.reset_timer_mod)
        root.setTabOrder(self.reset_timer_mod, self.mod_speaker_list)
        root.setTabOrder(self.mod_speaker_list, self.add_mod_caucus_button)
        root.setTabOrder(self.add_mod_caucus_button, self.add_mod_topic_field)
        root.setTabOrder(self.add_mod_topic_field, self.duration_spin_box)
        root.setTabOrder(self.duration_spin_box, self.speaking_time_spin_box)
        root.setTabOrder(self.speaking_time_spin_box, self.cancel_button_mod)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "MUN App"))
        self.delegates_title_label.setText(_translate("root", "Delegates"))
        self.add_delegate_button.setText(_translate("root", "Add Delegate"))
        self.add_delegate_page_title.setText(_translate("root", "Add Delegate"))
        self.cancel_button.setText(_translate("root", "Cancel"))
        self.confirm_add_button.setText(_translate("root", "Add Delegate"))
        self.points_and_motions_label.setText(_translate("root", "Points and Motions"))
        self.add_motion_button.setText(_translate("root", "Add Motion"))
        self.start_timer_mod.setText(_translate("root", "Start "))
        self.pause_timer_mod.setText(_translate("root", "Pause/Resume"))
        self.reset_timer_mod.setText(_translate("root", "Reset"))
        self.mod_speakers_list_label.setText(_translate("root", "Speakers "))
        self.mod_info_label.setText(_translate("root", "MOD INFO"))
        self.moderated_caucus_title_label.setText(_translate("root", "Moderated Caucus"))
        self.add_mod_caucus_button.setText(_translate("root", "Add Caucus"))
        self.add_mod_caucus_title.setText(_translate("root", "Add Moderated Caucus"))
        self.add_speaking_time_label.setText(_translate("root", "Speaking Time(Seconds)"))
        self.add_topic_label.setText(_translate("root", "Topic"))
        self.add_duration_label.setText(_translate("root", "Duration(Minutes)"))
        self.motioned_by_label.setText(_translate("root", "Motioned By"))
        self.first_or_last_label.setText(_translate("root", "First or Last Speech?"))
        self.first_speech_button.setText(_translate("root", "First "))
        self.last_speech_button.setText(_translate("root", "Last"))
        self.cancel_button_mod.setText(_translate("root", "Cancel"))
        self.confirm_add_button_mod.setText(_translate("root", "Add Caucus"))
        self.settings_title_label.setText(_translate("root", "Settings"))
        self.conference_title_label.setText(_translate("root", "Name of Conference"))
        self.committee_title_label.setText(_translate("root", "Committee Title "))
        self.chair_label.setText(_translate("root", "Chair"))
        self.co_chair_label.setText(_translate("root", "Co-Chair"))
        self.save_button.setText(_translate("root", "Save"))
        self.crisis_button.setText(_translate("root", "Crisis"))
        self.gap_button.setText(_translate("root", "GAP"))
        self.ga_button.setText(_translate("root", "GA"))
        self.cd_label.setText(_translate("root", "Crisis Director"))
        self.app_title.setText(_translate("root", "MUN APP"))
        self.delegates_button.setText(_translate("root", "Delegates"))
        self.settings_button.setText(_translate("root", "Settings"))
        self.points_motions_button.setText(_translate("root", "Points/Motions"))
        self.home_button.setText(_translate("root", "Home"))
        self.moderated_caucus_button.setText(_translate("root", "Moderated Caucus"))

import resources
