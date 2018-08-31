import sys
import os
import jsonpickle
import simplejson
import sip
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from settings import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog,QSizePolicy
import math
import time
from moderated_caucus import ModeratedCaucus
import resources
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QtWidgets.QWidget):

    def __init__(self, settings, app):
        super(MainWindow, self).__init__()
        self.center()
        self.settings = settings
        self.caucus = ModeratedCaucus(0, 30, 'default topic')
        self.defualt_unmod_time_value = 30
        munapp_ui = resource_path('mun_app_ui.ui')
        uic.loadUi(munapp_ui, self)
        self.countdown_value_mod = 30
        self.countdown_value_unmod = 30
        self.timer_state = False
        self.countdown_timer.setDigitCount(
            len(getTime(self.countdown_value_mod)))
        self.unmod_timer.setDigitCount(len(getTime(self.countdown_value_mod)))
        
        self.countdown_timer.display(getTime(self.countdown_value_mod))
        self.unmod_timer.display(getTime(self.countdown_value_unmod))

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
        self.unmod_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(6))
        self.stats_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(7))
        self.settings_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(8))

        #Home Page
        self.welcome_to_conference_label.setText('Welcome to ' + self.settings.conference_name +'!')
        self.image_path_label.setText(self.settings.image)
        pixmap = QPixmap(self.settings.image)
        # pixmap = pixmap.scaled(self.home_img_label.size(),Qt.KeepAspectRatio)
        self.home_img_label.setPixmap(pixmap)
        self.home_delegates_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(1))
        self.home_pm_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(3))
        self.home_mod_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(4))
        self.home_unmod_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(6))
        self.home_stats_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(7))
        self.home_settings_button.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(8))
        if(self.settings.committee_type.lower() == 'crisis'):
            self.home_cd_label.setText('Crisis Director: ' + self.settings.crisis_director_name)
            self.home_cd_label.show()
        else:
            print(self.settings.committee_type)
            self.home_cd_label.hide()

       # Settings Page
        self.crisis_button.clicked.connect(self.onCrisisClicked)
        self.ga_button.clicked.connect(self.onGaClicked)
        self.gap_button.clicked.connect(self.onGapClicked)
        self.conference_title_field.setText(self.settings.conference_name)
        self.home_committee_label.setText('Committee: ' +self.settings.committee_name)
        self.home_chair_label.setText('Chair: ' + self.settings.chair_name)
        self.home_co_label.setText('Co-Chair: ' + self.settings.co_chair_name)
        if(self.settings.committee_type.lower() == 'crisis'):
            self.home_cd_label.setText('Crisis Director: ' + self.settings.crisis_director_name)
        else:
            self.home_cd_label.hide()
        self.committee_title_field.setText(self.settings.committee_name)
        self.chair_field.setText(self.settings.chair_name)
        self.co_chair_field.setText(self.settings.co_chair_name)
        self.cd_field.setText(self.settings.crisis_director_name)
        self.save_button.clicked.connect(self.onSaveClicked)
        self.add_image_button.clicked.connect(self.addImageClicked)
        self.reset_image_button.clicked.connect(self.resetImage)
        self.image_path_label.setText(self.settings.image)

        self.image_label.hide()
        self.image_path_label.hide()
        self.reset_image_button.hide()
        self.add_image_button.hide()
        self.resetImage()

        # Delegates Page
        self.order_delegates_button.clicked.connect(self.onOrderDelegates)
        self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                          ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
        for i in range(len(self.settings.delegates)):

            delegate_ui = resource_path('delegate_view.ui')

            del_view = uic.loadUi(delegate_ui)
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
        self.addMotionView()

        # Add Moderated Caucus Page
        self.cancel_button_mod.clicked.connect(
            lambda: self.content_pane.setCurrentIndex(4))
        self.confirm_add_button_mod.clicked.connect(
            lambda: self.addModeratedCaucus())
        self.reset_motions_button.clicked.connect(lambda: self.resetMotions())
        
        # Mod
        self.start_timer_mod.clicked.connect(lambda: self.startTimer('mod'))
        self.pause_timer_mod.clicked.connect(lambda: self.pauseTimer('mod'))
        self.reset_timer_mod.clicked.connect(lambda: self.resetTimer('mod'))
        self.add_ext_button.clicked.connect(self.addExtClicked)
        self.cancel_add_ext.clicked.connect(lambda: self.add_ext_stack.setCurrentIndex(0))
        self.confirm_add_ext.clicked.connect(lambda:self.addExtension())
        # Unmod
        self.unmod_timer_start_button.clicked.connect(
            lambda: self.startTimer('unmod'))
        self.unmod_timer_pause_button.clicked.connect(
            lambda: self.pauseTimer('unmod'))
        self.unmod_timer_reset_button.clicked.connect(
            lambda: self.resetTimer('unmod'))
        self.add_unmod_button.clicked.connect(
            lambda: self.add_unmod_widget.setCurrentIndex(1))
        self.cancel_set_unmod.clicked.connect(
            lambda: self.add_unmod_widget.setCurrentIndex(0))
        self.confirm_set_unmod.clicked.connect(lambda:  self.setUnmod(
            self.set_unmod_min_spinbox.value() * 60 + self.set_unmod_sec_spinbox.value()))

        # Data

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)
        # self.figure.tight_layout()
        self.figure.patch.set_facecolor('#4B9CD3')
        self.ax.set_facecolor("#13294B")
        self.stats_layout.addWidget(self.canvas)
        self.updateData()

   #------------------------------------Functionality------------------------------------#
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


    def updateData(self):
        sort = sorted(settings.delegates, key=lambda x: x.title.lower())
        self.ax.cla()
        y = []
        if(sort):
            for delegate in sort:
                self.ax.bar(delegate.title, delegate.times_called_on)
                y.append(delegate.times_called_on)
            for tick in self.ax.get_xticklabels():
                # tick.set_rotation(45)
                tick.set_fontsize(10)
            yint = range(min(y), math.ceil(max(y))+1)
            self.figure.autofmt_xdate()
            self.ax.set_yticks(yint)
        self.figure.tight_layout()
        self.settings.toJSON()
        self.canvas.draw()
    # Delegates Page Functions
    def onOrderDelegates(self):
        self.settings.delegates.sort(key = lambda x : x.title.lower())
        self.settings.toJSON()
        for i in reversed(range(self.dels_layout.count())): 
            self.dels_layout.itemAt(i).widget().setParent(None)
        for delegate in self.settings.delegates:
            delegate_ui = resource_path('delegate_view.ui')
            del_view = uic.loadUi(delegate_ui)
            del_view.delegate_name_label.setText(delegate.title)
            del_view.present_button.clicked.connect(
                lambda _, b=del_view: self.onPresentClicked(b))
            del_view.absent_button.clicked.connect(
                lambda _, b=del_view: self.onAbsentClicked(b))
            del_view.delete_delegate_button.clicked.connect(
                lambda _, b=del_view: self.deleteDelegate(b))

            self.dels_layout.addWidget(del_view)
    


    def deleteDelegate(self, widget):
        delegate_name = widget.delegate_name_label.text().strip()
        self.dels_layout.removeWidget(widget)
        widget.hide()
        widget = None
        for delegate in settings.delegates:
            if delegate.title.lower() == delegate_name.lower():
                if delegate.isPresent:
                    settings.total_present_delegates -= 1
                    self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                                      ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
                self.settings.delegates.remove(delegate)
                self.settings.toJSON()
                self.updateData()
                self.removeItemComboBox(delegate.title)

    def onAddDelButtonClicked(self):
        self.content_pane.setCurrentIndex(2)
        self.add_delegate_name_field.setText('Delegate Name')
        self.add_delegate_name_field.setSelection(0, 100)
        self.add_delegate_name_field.setFocus()

    def onPresentClicked(self, widget):
        delegate_name = widget.delegate_name_label.text().strip()
        for delegate in settings.delegates:
            if delegate.title.lower() == delegate_name.lower():
                if not(delegate.isPresent):
                    self.settings.total_present_delegates += 1
                    self.delegates_info_label.setText('Total Delegates: ' + str(len(self.settings.delegates)) + ' | Total Present Delegates: ' + str(self.settings.total_present_delegates) +
                                                      ' | Simple Majority: ' + str(int(self.settings.total_present_delegates / 2 + 1)) + '  | 2/3 Majority: ' + str(int(math.ceil(2/3*self.settings.total_present_delegates))))
                delegate.isPresent = True
                self.settings.toJSON()

    def onAbsentClicked(self, widget):
        delegate_name = widget.delegate_name_label.text().strip()
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
            Delegate(self.add_delegate_name_field.text().strip()))
        self.settings.toJSON()
        self.updateData()
        self.dels_layout.setAlignment(Qt.AlignTop)

        delegate_ui = resource_path('delegate_view.ui')

        del_view = uic.loadUi(delegate_ui)

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
        self.updateData()
    # Settings Page Button Functions
    def resetImage(self):
        pixmap = QPixmap(':/img/resources/united-nations-logo.png')
        pixmap = pixmap.scaled(self.home_img_label.size(),Qt.KeepAspectRatio)
        self.home_img_label.setPixmap(pixmap)
        self.image_path_label.setText(':/img/resources/united-nations-logo.png')
        self.settings.image = ':/img/resources/united-nations-logo.png'
        self.settings.toJSON()
    def addImageClicked(self): 
        fileName, dummy = QFileDialog.getOpenFileName(None, "Open image file...")
        fileName = fileName.lower()
        if('jpg' in fileName or 'png' in fileName or 'jpeg' in fileName or 'bmp' in fileName or 'ico' in fileName):
            self.settings.image = fileName
            self.settings.toJSON
            self.image_path_label.setText(self.settings.image)
            pixmap = QPixmap(self.settings.image)
            pixmap = pixmap.scaled(self.home_img_label.size(),Qt.KeepAspectRatio)
            self.home_img_label.setPixmap(pixmap)

    def onCrisisClicked(self):
        self.settings.committeeType = 'Crisis'
        self.cd_label.show()
        self.cd_field.show()
        self.settings.toJSON

    def onGaClicked(self):
        self.settings.committee_type = 'GA'
        self.cd_label.hide()
        self.cd_field.hide()
        self.settings.toJSON

    def onGapClicked(self):
        self.settings.committee_type = 'GAP'
        self.cd_label.hide()
        self.cd_field.hide()
        self.settings.toJSON

    def onSaveClicked(self):
        self.settings.conference_name = self.conference_title_field.text().strip()
        self.settings.committee_name = self.committee_title_field.text().strip()
        self.settings.chair_name = self.chair_field.text().strip()
        self.settings.co_chair_name = self.co_chair_field.text().strip()
        if(self.crisis_button.isChecked()):
            self.settings.committeeType = 'Crisis'
            self.settings.crisis_director_name = self.cd_field.text().strip()
        elif(self.ga_button.isChecked()):
            self.settings.crisis_director_name = ''
            self.settings.committee_type = 'GA'
        else:
            self.settings.crisis_director_name = ''
            self.settings.committee_type = 'GAP'
        self.welcome_to_conference_label.setText('Welcome to ' + self.settings.conference_name +'!')
        self.image_path_label.setText(self.settings.image)
        pixmap = QPixmap(self.settings.image)
        pixmap = pixmap.scaled(self.home_img_label.size(),Qt.KeepAspectRatio)
        self.home_img_label.setPixmap(pixmap)
        self.home_committee_label.setText('Committee: ' +self.settings.committee_name)
        self.home_chair_label.setText('Chair: ' + self.settings.chair_name)
        self.home_co_label.setText('Co-Chair: ' + self.settings.co_chair_name)
        if(self.settings.committee_type.lower() == 'crisis'):
            self.home_cd_label.setText('Crisis Director: ' + self.settings.crisis_director_name)
            self.home_cd_label.show()
        else:
            self.home_cd_label.hide()
        self.settings.toJSON()

    # Points and Motions Button Functions
    def resetMotions(self):
        for view in self.motion_views:
            view.hide()
        self.addMotionView()
    def addMotionView(self):

        motion_options = resource_path('motion_options.ui')
        self.motion_views.append(uic.loadUi(motion_options))
        self.motion_views[-1].delegates_combo_box.setEditable(True)
        self.motion_views[-1].delegates_combo_box.lineEdit().setReadOnly(True)
        self.motion_views[-1].delegates_combo_box.lineEdit(
        ).setAlignment(QtCore.Qt.AlignCenter)
        self.points_motions_layout.addWidget(self.motion_views[-1])
        for delegate in self.settings.delegates:
            self.motion_views[-1].delegates_combo_box.addItem(
                delegate.title, delegate)
            self.motion_views[-1].delegates_combo_box.model().sort(0)
        self.motion_views[-1].start_motion_button.clicked.connect(
            lambda _, b=self.motion_views[-1]: self.startCaucusFromMotions(b))

    def startCaucusFromMotions(self, b):
        if(b.mod_check_box.isChecked()):
            self.caucus = ModeratedCaucus(b.doubleSpinBox.value(), b.spinBox.value(
            ), b.topic_line_edit.text().strip(), b.delegates_combo_box.currentData(), b.first_check_box.isChecked())
            for i in reversed(range(self.speaker_list_layout.count())):
                self.speaker_list_layout.itemAt(i).widget().setParent(None)
            self.setUpMod(self.caucus.duration,
                          self.caucus.speaking_time, self.caucus.topic)
        elif(b.unmod_check_box.isChecked()):
            self.defualt_unmod_time_value = int(b.doubleSpinBox.value() * 60)
            self.resetTimer('unmod')
            self.content_pane.setCurrentIndex(6)

    def addItemComboBox(self, delegate):
        for view in self.motion_views:
            view.delegates_combo_box.addItem(delegate.title, delegate)
            view.delegates_combo_box.setItemData(1, 1, Qt.UserRole)

    def removeItemComboBox(self, name):
        for view in self.motion_views:
            for i in range(view.delegates_combo_box.count()):
                if(view.delegates_combo_box.itemText(i) == name):
                    view.delegates_combo_box.removeItem(i)

    # Add Mod Functions
    def addModPressed(self):
        self.motioned_by_combo_box.clear()
        for delegate in self.settings.delegates:
            self.motioned_by_combo_box.addItem(delegate.title, delegate)
            # self.motioned_by_combo_box.setItemData(1, 1, Qt.UserRole)

        self.content_pane.setCurrentIndex(5)

    def addModeratedCaucus(self):
        self.caucus = ModeratedCaucus(self.duration_spin_box.value(
        ), self.speaking_time_spin_box.value(), self.add_mod_topic_field.text().strip(), self.motioned_by_combo_box.currentData(), self.first_speech_button.isChecked())
        for i in reversed(range(self.speaker_list_layout.count())):
            self.speaker_list_layout.itemAt(i).widget().setParent(None)
        self.setUpMod(self.caucus.duration,
                      self.caucus.speaking_time, self.caucus.topic)
        self.updateData()

    def setUpMod(self, duration, speaking_time, topic):
        self.speaker_list_layout.setAlignment(Qt.AlignTop)
        if (duration * 60 / speaking_time).is_integer():
            num_speakers = (duration * 60 / speaking_time)
        else:
            return
        for i in range(int(num_speakers)):
            speaker_view = resource_path('speaker_view.ui')
            speaker_view = uic.loadUi(speaker_view)
            speaker_view.add_speaker_button.clicked.connect(
                lambda _, b=speaker_view: self.onAddSpeakerClicked(b))
            speaker_view.cancel_speaker_button.clicked.connect(
                lambda _, b=speaker_view: self.onCancelSpeakerClicked(b))
            speaker_view.confirm_speaker_button.clicked.connect(
                lambda _, b=speaker_view: self.onConfirmSpeakerClicked(b))

            for delegate in self.settings.delegates:
                speaker_view.add_speaker_combo_box.addItem(
                    delegate.title, delegate)
            speaker_view.speaker_number_label.setText(str(i+1))
            if(self.caucus.is_first_speaker and i == 0):
                speaker_view.speaker_name_label.setText(
                    self.caucus.motioned_by.title)
            elif(not self.caucus.is_first_speaker and i == num_speakers - 1):
                speaker_view.speaker_name_label.setText(
                    self.caucus.motioned_by.title)

            self.speaker_list_layout.addWidget(speaker_view)

        self.caucus.motioned_by.times_called_on += 1
        self.updateData()
        self.mod_info_label.setText(
            str(duration) + ' minute ' + str(speaking_time) + ' second caucus on ' + topic)
        self.countdown_value_mod = speaking_time
        self.content_pane.setCurrentIndex(4)
        if(self.countdown_value_mod > 99):
            self.countdown_timer.setDigitCount(4)
        elif(self.countdown_value_mod >= 10):
            self.countdown_timer.setDigitCount(4)
        else:
            self.countdown_value_mod.setDigitCount(4)
        self.countdown_timer.display(getTime(self.countdown_value_mod))

    def onAddSpeakerClicked(self, b):
        b.setCurrentIndex(1)

    def onCancelSpeakerClicked(self, b):
        b.setCurrentIndex(0)
    def addExtClicked(self):
        for delegate in self.settings.delegates:
            self.ext_combo_box.addItem(delegate.title, delegate)
            self.add_ext_stack.setCurrentIndex(1)

    def addExtension(self):
        duration = self.ext_spin_box.value()
        self.speaker_list_layout.setAlignment(Qt.AlignTop)
        self.ext_combo_box.currentData().times_called_on += 1
        self.updateData()
        if((duration * 60 / self.caucus.speaking_time).is_integer() and not duration == 0):
            num_extra_speakers = (duration * 60 / self.caucus.speaking_time)
            for i in range(int(num_extra_speakers) + 1):
                speaker_view = resource_path('speaker_view.ui')
                speaker_view = uic.loadUi(speaker_view)
                if i == 0:
                    speaker_view.setCurrentIndex(2)
                
                speaker_view.add_speaker_button.clicked.connect(
                    lambda _, b=speaker_view: self.onAddSpeakerClicked(b))
                speaker_view.cancel_speaker_button.clicked.connect(
                    lambda _, b=speaker_view: self.onCancelSpeakerClicked(b))
                speaker_view.confirm_speaker_button.clicked.connect(
                    lambda _, b=speaker_view: self.onConfirmSpeakerClicked(b))

                for delegate in self.settings.delegates:
                    speaker_view.add_speaker_combo_box.addItem(
                        delegate.title, delegate)
                num_prev = int(self.caucus.duration * 60 / self.caucus.speaking_time)
                speaker_view.speaker_number_label.setText(str(i+num_prev))
                if(self.ext_first.isChecked() and i == 1):
                    speaker_view.speaker_name_label.setText(
                        self.ext_combo_box.currentData().title)
                elif(not self.ext_first.isChecked() and i == num_extra_speakers):
                    speaker_view.speaker_name_label.setText(
                        self.ext_combo_box.currentData().title)
                
                self.speaker_list_layout.addWidget(speaker_view)
            self.add_ext_stack.setCurrentIndex(0)
            
    def onConfirmSpeakerClicked(self, b):
        delegate = b.add_speaker_combo_box.currentData()
        b.speaker_name_label.setText(delegate.title)
        delegate.times_called_on += 1
        self.updateData()
        self.settings.toJSON()
        self.updateData()
        b.setCurrentIndex(0)

    def startTimer(self, mode):
        self.timer_state = True
        if(mode == 'mod'):
            for tick in range(self.countdown_value_mod, -1, -1):
                self.countdown_timer.setDigitCount(
                    len(getTime(self.countdown_value_mod - 1)))
                if(self.timer_state):
                    self.countdown_value_mod = self.countdown_value_mod - 1
                    self.countdown_timer.display(
                        getTime(self.countdown_value_mod))
                    self.start_timer_mod.setEnabled(not tick)
                    start = time.time()
                    while time.time() - start < 1:
                        app.processEvents()
                        time.sleep(0.02)
        else:
            for tick in range(self.countdown_value_unmod, -1, -1):
                self.unmod_timer.setDigitCount(
                    len(getTime(self.countdown_value_unmod)))
                if(self.timer_state):
                    self.countdown_value_unmod = self.countdown_value_unmod - 1
                    self.unmod_timer.display(
                        getTime(self.countdown_value_unmod))
                    self.unmod_timer_start_button.setEnabled(not tick)
                    start = time.time()
                    while time.time() - start < 1:
                        app.processEvents()
                        time.sleep(0.02)

    def pauseTimer(self, mode):
        if(self.timer_state):
            self.timer_state = False
        else:
            self.timer_state = True
            self.startTimer(mode)

    def resetTimer(self, mode):
        if(self.timer_state):
            self.pauseTimer(mode)

        self.timer_state = False
        if(mode == 'mod'):
            self.countdown_value_mod = self.caucus.speaking_time
            self.countdown_timer.setDigitCount(
                len(getTime(self.countdown_value_mod)))
            self.countdown_timer.display(getTime(self.countdown_value_mod))
            self.start_timer_mod.setEnabled(True)
        else:
            self.countdown_value_unmod = self.defualt_unmod_time_value
            self.unmod_timer.setDigitCount(
                len(getTime(self.countdown_value_unmod)))
            self.unmod_timer.display(getTime(self.countdown_value_unmod))
            self.unmod_timer_start_button.setEnabled(True)

    # Unmod
    def setUnmod(self, seconds):
        self.defualt_unmod_time_value = seconds
        self.countdown_value_unmod = self.defualt_unmod_time_value
        self.resetTimer('unmod')
        self.add_unmod_widget.setCurrentIndex(0)


def getTime(time):
    minutes = math.floor(time / 60)
    seconds = time % 60
    if(seconds < 10):
        seconds = '0'+str(seconds)
    if(minutes != 0):
        return str(minutes) + ':' + str(seconds)
    else:
        return ':' + str(seconds)


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle(QtWidgets.QStyleFactory.create('fusion'))

    json = resource_path('config.json')

    try:
        file = open(json, 'r')

    except IOError:
        file = open(json, 'w')

    if(os.stat(json).st_size == 0):
        settings = Settings()

    else:
        with open(json, 'r') as file:
            jsonpickle.set_preferred_backend('simplejson')
            settings = jsonpickle.decode(file.read())

    window = MainWindow(settings, app)
    
    window.content_pane.setCurrentIndex(0)

    window.show()
    sys.exit(app.exec_())
