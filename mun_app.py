import sys
import os
import jsonpickle
import sip
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from settings import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
import time
from moderated_caucus import ModeratedCaucus


class MainWindow(QtWidgets.QWidget):

    def __init__(self, settings, app):
        super(MainWindow, self).__init__()
        self.settings = settings
        uic.loadUi('ui_files/mun_app_ui.ui', self)

        self.countdown_value = 30
        self.timer_state = False

        # Content Navigation
        self.home_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(0))
        self.delegates_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(1))
        self.add_delegate_button.clicked.connect(self.onAddDelButtonClicked)
        self.points_motions_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(3))
        self.moderated_caucus_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(4))
        self.add_mod_caucus_button.clicked.connect(
            lambda: self.addModPressed())
        self.settings_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(6))

       # Settings Page
        self.crisis_button.clicked.connect(self.onCrisisClicked)
        self.ga_button.clicked.connect(self.onGaClicked)
        self.gap_button.clicked.connect(self.onGapClicked)
        self.conference_title_field.setText(settings.conference_name)
        self.committee_title_field.setText(settings.committee_name)
        self.chair_field.setText(settings.chair_name)
        self.co_chair_field.setText(settings.co_chair_name)
        self.cd_field.setText(settings.crisis_director_name)
        self.save_button.clicked.connect(self.onSaveClicked)

        # Delegates Page
        self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                          ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
        for i in range(len(self.settings.delegates)):
            del_view = uic.loadUi('ui_files/delegate_view.ui')
            self.dels_layout.setAlignment(Qt.AlignTop)

            delegate = self.settings.delegates[i]

            if(delegate.isPresent):
                del_view.present_button.setChecked(True)
                del_view.absent_button.setChecked(False)
            else:
                del_view.present_button.setChecked(False)
                del_view.absent_button.setChecked(True)

            del_view.delegate_name_label.setText(delegate.title)
            del_view.delete_delegate_button.clicked.connect(
                lambda _, b=del_view: self.deleteDelegate(b))

            del_view.present_button.clicked.connect(
                lambda _, b=del_view: self.onPresentClicked(b))
            del_view.absent_button.clicked.connect(
                lambda _, b=del_view: self.onAbsentClicked(b))

            self.dels_layout.addWidget(del_view)

        # Add Delegate Page
        self.cancel_button.clicked.connect(self.onCancelButtonPressed)
        self.confirm_add_button.clicked.connect(
            self.onConfirmAddDelegatePressed)

        # Points and Motions Page
        self.motion_views = []
        self.points_motions_layout.setAlignment(Qt.AlignTop)
        self.add_motion_button.clicked.connect(self.addMotionView)
        for i in range(3):
            self.addMotionView()

        # Add Moderated Caucus Page
        self.cancel_button_mod.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(4))
        self.confirm_add_button_mod.clicked.connect(
            lambda: self.addModeratedCaucus())

        # Mod
        self.start_timer_mod.clicked.connect(lambda: self.startTimer())
        self.pause_timer_mod.clicked.connect(lambda: self.pauseTimer())
        self.reset_timer_mod.clicked.connect(lambda: self.resetTimer())
   #------------------------------------Functionality------------------------------------#

    # Delegates Page Functions
    def deleteDelegate(self, widget):
        delegate_name = widget.delegate_name_label.text()
        self.dels_layout.removeWidget(widget)
        sip.delete(widget)
        widget = None
        for delegate in settings.delegates:
            if delegate.title.lower() == delegate_name.lower():
                if delegate.isPresent:
                    settings.total_present_delegates -= 1
                    self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                                      ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
                self.settings.delegates.remove(delegate)
                self.settings.toJSON()
                self.removeItemComboBox(delegate.title)

    def onAddDelButtonClicked(self):
        self.content_pane.setCurrentIndex(2)
        self.add_delegate_name_field.setText('Delegate Name')
        self.add_delegate_name_field.setSelection(0, 100)
        self.add_delegate_name_field.setFocus()

    def onPresentClicked(self, widget):
        delegate_name = widget.delegate_name_label.text()
        for delegate in settings.delegates:
            if delegate.title.lower() == delegate_name.lower():
                if not(delegate.isPresent):
                    self.settings.total_present_delegates += 1
                    self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                                      ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
                delegate.isPresent = True
                self.settings.toJSON()

    def onAbsentClicked(self, widget):
        delegate_name = widget.delegate_name_label.text()
        for delegate in settings.delegates:
            if delegate.title.lower() == delegate_name.lower():
                if delegate.isPresent:
                    self.settings.total_present_delegates -= 1
                    self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                                      ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
                delegate.isPresent = False
                self.settings.toJSON()

    # Add Delegate Button Functions
    def onCancelButtonPressed(self):
        self.content_pane.setCurrentIndex(1)

    def onConfirmAddDelegatePressed(self):
        self.settings.delegates.append(
            Delegate(self.add_delegate_name_field.text()))
        self.settings.toJSON()
        self.dels_layout.setAlignment(Qt.AlignTop)
        del_view = uic.loadUi('ui_files\delegate_view.ui')

        delegate = self.settings.delegates[-1]
        del_view.delegate_name_label.setText(delegate.title)
        del_view.present_button.clicked.connect(
            lambda _, b=del_view: self.onPresentClicked(b))
        del_view.absent_button.clicked.connect(
            lambda _, b=del_view: self.onAbsentClicked(b))
        del_view.delete_delegate_button.clicked.connect(
            lambda _, b=del_view: self.deleteDelegate(b))

        self.dels_layout.addWidget(del_view)
        self.content_pane.setCurrentIndex(1)
        self.addItemComboBox(delegate)
        self.settings.total_present_delegates += 1
        self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                          ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
        self.settings.toJSON()
    # Settings Page Button Functions

    def onCrisisClicked(self):
        self.settings.committeeType = 'Crisis'
        self.cd_label.show()
        self.cd_field.show()
        settings.toJSON

    def onGaClicked(self):
        self.settings.committee_type = 'GA'
        self.cd_label.hide()
        self.cd_field.hide()
        settings.toJSON

    def onGapClicked(self):
        self.settings.committee_type = 'GAP'
        self.cd_label.hide()
        self.cd_field.hide()
        self.settings.toJSON

    def onSaveClicked(self):
        self.settings.conference_name = self.conference_title_field.text()
        self.settings.committee_name = self.committee_title_field.text()
        self.settings.chair_name = self.chair_field.text()
        self.settings.co_chair_name = self.co_chair_field.text()
        if(self.crisis_button.isChecked()):
            self.settings.committeeType = 'Crisis'
            self.settings.crisis_director_name = self.cd_field.text()
        elif(self.ga_button.isChecked()):
            self.settings.crisis_director_name = ''
            self.settings.committee_type = 'GA'
        else:
            self.settings.crisis_director_name = ''
            self.settings.committee_type = 'GAP'
        self.settings.toJSON()

    # Points and Motions Button Functions
    def addMotionView(self):
        self.motion_views.append(uic.loadUi('ui_files/motion_options.ui'))
        self.motion_views[-1].delegates_combo_box.setEditable(True)
        self.motion_views[-1].delegates_combo_box.lineEdit().setReadOnly(True)
        self.motion_views[-1].delegates_combo_box.lineEdit(
        ).setAlignment(QtCore.Qt.AlignCenter)
        self.points_motions_layout.addWidget(self.motion_views[-1])
        for delegate in self.settings.delegates:
            self.motion_views[-1].delegates_combo_box.addItem(delegate.title,delegate)
            self.motion_views[-1].delegates_combo_box.model().sort(0)
        self.motion_views[-1].start_motion_button.clicked.connect(lambda _, b=self.motion_views[-1]: self.startModFromMotions(b))

    def startModFromMotions(self,b):
        self.caucus = ModeratedCaucus(b.doubleSpinBox.value(),b.spinBox.value(),b.lineEdit.text(),b.delegates_combo_box.currentData(), b.first_check_box.isChecked())
        for i in reversed(range(self.speaker_list_layout.count())):
            self.speaker_list_layout.itemAt(i).widget().setParent(None)

        self.setUpMod(self.caucus.duration,
                      self.caucus.speaking_time, self.caucus.topic)

    def addItemComboBox(self, delegate):
        for view in self.motion_views:
            view.delegates_combo_box.addItem(delegate.title,delegate)
            view.delegates_combo_box.setItemData(1, 1, Qt.UserRole)

    def removeItemComboBox(self, name):
        for view in self.motion_views:
            for i in range(view.delegates_combo_box.count()):
                if(view.delegates_combo_box.itemText(i) == name):
                    view.delegates_combo_box.removeItem(i)

    # Add Mod Functions
    def addModPressed(self):
        for delegate in self.settings.delegates:
            self.motioned_by_combo_box.addItem(delegate.title, delegate)
            self.motioned_by_combo_box.setItemData(1, 1, Qt.UserRole)

        self.content_pane.setCurrentIndex(5)

    def addModeratedCaucus(self):
        self.caucus = ModeratedCaucus(self.duration_spin_box.value(
        ), self.speaking_time_spin_box.value(), self.add_mod_topic_field.text(), self.motioned_by_combo_box.currentData(), self.first_speech_button.isChecked())
        for i in reversed(range(self.speaker_list_layout.count())):
            self.speaker_list_layout.itemAt(i).widget().setParent(None)

        self.setUpMod(self.caucus.duration,
                      self.caucus.speaking_time, self.caucus.topic)

    def setUpMod(self, duration, speaking_time, topic):
        self.speaker_list_layout.setAlignment(Qt.AlignTop)
        if (duration * 60 / speaking_time).is_integer():
            num_speakers = (duration * 60 / speaking_time)
        else:
            return
        for i in range(int(num_speakers)):
            speaker_view = uic.loadUi('ui_files\speaker_view.ui')
            speaker_view.add_speaker_button.clicked.connect(lambda _, b=speaker_view: self.onAddSpeakerClicked(b))
            speaker_view.cancel_speaker_button.clicked.connect(lambda _, b=speaker_view: self.onCancelSpeakerClicked(b))
            speaker_view.confirm_speaker_button.clicked.connect(lambda _, b=speaker_view: self.onConfirmSpeakerClicked(b))


            for delegate in self.settings.delegates:
                speaker_view.add_speaker_combo_box.addItem(delegate.title,delegate)
            speaker_view.speaker_number_label.setText(str(i+1))
            if(self.caucus.is_first_speaker and i == 0):
                speaker_view.speaker_name_label.setText(
                    self.caucus.motioned_by.title)
            elif(not self.caucus.is_first_speaker and i == num_speakers - 1):
                speaker_view.speaker_name_label.setText(
                    self.caucus.motioned_by.title)

            self.speaker_list_layout.addWidget(speaker_view)

        self.mod_info_label.setText(
            str(duration) + ' minute ' + str(speaking_time) + ' second caucus on ' + topic)
        self.countdown_value = speaking_time
        self.content_pane.setCurrentIndex(4)
        if(self.countdown_value > 99):
            self.countdown_timer.setDigitCount(3)
        elif(self.countdown_value >= 10):
            self.countdown_timer.setDigitCount(2)
        else:
            self.countdown_value.setDigitCount(1)
        self.countdown_timer.display(self.countdown_value)

    def onAddSpeakerClicked(self,b):
        b.setCurrentIndex(1)

    
    def onCancelSpeakerClicked(self,b):
        b.setCurrentIndex(0)

    def onConfirmSpeakerClicked(self,b):
        b.speaker_name_label.setText(b.add_speaker_combo_box.currentText())
        b.setCurrentIndex(0)

    def startTimer(self):
        self.timer_state = True
        for tick in range(self.countdown_value, -1, -1):
            if(self.countdown_value - 1 > 99):
                self.countdown_timer.setDigitCount(3)
            elif(self.countdown_value - 1 >= 10):
                self.countdown_timer.setDigitCount(2)
            else:
                self.countdown_timer.setDigitCount(1)
            if(self.timer_state):
                self.countdown_value = self.countdown_value - 1
                self.countdown_timer.display(self.countdown_value)
                self.start_timer_mod.setEnabled(not tick)
                start = time.time()
                while time.time() - start < 1:
                    app.processEvents()
                    time.sleep(0.02)

    def pauseTimer(self):
        if(self.timer_state):
            self.timer_state = False
        else:
            self.timer_state = True
            self.startTimer()

    def resetTimer(self):
        if(self.timer_state):
            self.pauseTimer()

        self.timer_state = False
        self.countdown_value = self.caucus.speaking_time
        if(self.countdown_value > 99):
            self.countdown_timer.setDigitCount(3)
        elif(self.countdown_value >= 10):
            self.countdown_timer.setDigitCount(2)
        else:
            self.countdown_timer.setDigitCount(1)

        self.countdown_timer.display(self.countdown_value)
        self.start_timer_mod.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if(os.stat('config.json').st_size == 0):
        settings = Settings()
    else:
        with open('config.json', 'r') as file:
            settings = jsonpickle.decode(file.read())

    window = MainWindow(settings, app)
    window.content_pane.setCurrentIndex(0)
    window.show()
    sys.exit(app.exec_())
