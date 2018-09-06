from math import floor, ceil
import sys,os
from PyQt5 import uic
from PyQt5 import QtCore,QtGui,QtWidgets
import csv
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from settings import Delegate
from moderated_caucus import ModeratedCaucus
import time

def update_del_info_label(mun_app):
    mun_app.delegates_info_label.setText('Total Delegates: ' + str(len(mun_app.settings.delegates)) +
                                         ' | Total Present Delegates: ' + str(mun_app.settings.total_present_delegates) +
                                         ' | Simple Majority: ' + str(int(mun_app.settings.total_present_delegates / 2 + 1)) +
                                         '  | 2/3 Majority: ' + str(int(ceil(2/3*mun_app.settings.total_present_delegates))))


def getTime(time):
    minutes = floor(time / 60)
    seconds = time % 60
    if(seconds < 10):
        seconds = '0'+str(seconds)
    if(minutes != 0):
        return str(minutes) + ':' + str(seconds)
    else:
        return ':' + str(seconds)


def reset_data(mun_app):
    for delegate in mun_app.settings.delegates:
        delegate.times_called_on = 0
    mun_app.settings.toJSON()
    updateData(mun_app)
    mun_app.reset_data_widget.setCurrentIndex(0)


def updateData(mun_app):
    sort = sorted(mun_app.settings.delegates, key=lambda x: x.title.lower())
    mun_app.ax.cla()
    y = []
    if(sort):
        for delegate in sort:
            mun_app.ax.bar(delegate.title, delegate.times_called_on)
            y.append(delegate.times_called_on)
        for tick in mun_app.ax.get_xticklabels():
            # tick.set_rotation(45)
            tick.set_fontsize(10)
        yint = range(min(y), ceil(max(y))+1)
        mun_app.figure.autofmt_xdate()
        mun_app.ax.set_yticks(yint)
    mun_app.figure.tight_layout()
    mun_app.settings.toJSON()
    mun_app.canvas.draw()


def exportAttendence(mun_app):
    filename, thing = QFileDialog.getSaveFileName()
    with open(filename+'.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for delegate in mun_app.settings.delegates:
            if(delegate.isPresent):
                attendence_status = "Present"
            else:
                attendence_status = "Absent"
            writer.writerow([delegate.title, attendence_status])


def removeAllDelegates(mun_app):
    mun_app.rm_all_widget.setCurrentIndex(0)
    for i in reversed(range(mun_app.dels_layout.count())):
        mun_app.dels_layout.itemAt(i).widget().setParent(None)
    mun_app.settings.total_present_delegates = 0
    mun_app.settings.delegates = []
    update_del_info_label(mun_app)
    mun_app.settings.toJSON()
    updateData(mun_app)


def onOrderDelegates(mun_app):
    mun_app.settings.delegates.sort(key=lambda x: x.title.lower())
    mun_app.settings.toJSON()
    for i in reversed(range(mun_app.dels_layout.count())):
        mun_app.dels_layout.itemAt(i).widget().setParent(None)
    for delegate in mun_app.settings.delegates:
        delegate_ui = resource_path('delegate_view.ui')
        del_view = uic.loadUi(delegate_ui)
        del_view.delegate_name_label.setText(delegate.title)
        del_view.present_button.clicked.connect(
            lambda _, b=del_view: onPresentClicked(mun_app,b))
        del_view.absent_button.clicked.connect(
            lambda _, b=del_view: onAbsentClicked(mun_app,b))
        del_view.delete_delegate_button.clicked.connect(
            lambda _, b=del_view: deleteDelegate(mun_app,b))
        
        del_view.present_button.setChecked(delegate.isPresent)
        del_view.absent_button.setChecked(not delegate.isPresent)
        

        mun_app.dels_layout.addWidget(del_view)


def deleteDelegate(mun_app, widget):
    delegate_name = widget.delegate_name_label.text().strip()
    mun_app.dels_layout.removeWidget(widget)
    widget.setParent(None)
    for delegate in mun_app.settings.delegates:
        if delegate.title.lower() == delegate_name.lower():
            if delegate.isPresent:
                mun_app.settings.total_present_delegates -= 1

            mun_app.settings.delegates.remove(delegate)
            mun_app.settings.toJSON()
            updateData(mun_app)
            update_del_info_label(mun_app)
            removeItemComboBox(mun_app,delegate.title)

def onAddDelButtonClicked(mun_app):
    mun_app.content_pane.setCurrentIndex(2)
    mun_app.add_delegate_name_field.setText('Delegate Name')
    mun_app.add_delegate_name_field.setSelection(0, 100)
    mun_app.add_delegate_name_field.setFocus()

def onPresentClicked(mun_app, widget):
    delegate_name = widget.delegate_name_label.text().strip()
    for delegate in mun_app.settings.delegates:
        if delegate.title.lower() == delegate_name.lower():
            if not delegate.isPresent:
                mun_app.settings.total_present_delegates += 1
                update_del_info_label(mun_app)
            delegate.isPresent =True
            mun_app.settings.toJSON()

def onAbsentClicked(mun_app, widget):
    delegate_name = widget.delegate_name_label.text().strip()
    for delegate in mun_app.settings.delegates:
        if delegate.title.lower() == delegate_name.lower():
            if delegate.isPresent:
                mun_app.settings.total_present_delegates -= 1
                update_del_info_label(mun_app)
            delegate.isPresent = False
            mun_app.settings.toJSON()

# Add Delegate Button Functions
def onCancelButtonPressed(mun_app):
    mun_app.content_pane.setCurrentIndex(1)

def onConfirmAddDelegatePressed(mun_app):
    mun_app.settings.delegates.append(
        Delegate(mun_app.add_delegate_name_field.text().strip()))
    mun_app.settings.toJSON()
    mun_app.dels_layout.setAlignment(Qt.AlignTop)

    delegate_ui = resource_path('delegate_view.ui')

    del_view = uic.loadUi(delegate_ui)

    delegate = mun_app.settings.delegates[-1]
    del_view.delegate_name_label.setText(delegate.title)
   
    del_view.present_button.clicked.connect(
        lambda _, b=del_view: onPresentClicked(mun_app,b))
    del_view.absent_button.clicked.connect(
        lambda _, b=del_view: onAbsentClicked(mun_app,b))
    del_view.delete_delegate_button.clicked.connect(
        lambda _, b=del_view: deleteDelegate(mun_app,b))

    mun_app.dels_layout.addWidget(del_view)
    mun_app.content_pane.setCurrentIndex(mun_app.DELEGATES_INDEX)
    addItemComboBox(mun_app,delegate)
    mun_app.settings.total_present_delegates += 1
    update_del_info_label(mun_app)
    mun_app.settings.toJSON()
    updateData(mun_app)

def onCrisisClicked(mun_app):
    mun_app.settings.committee_type = 'Crisis'
    mun_app.cd_label.show()
    mun_app.cd_field.show()
    mun_app.home_cd_label.show()

    mun_app.settings.toJSON

def onGaClicked(mun_app):
    mun_app.settings.committee_type = 'GA'
    mun_app.cd_label.hide()
    mun_app.cd_field.hide()
    mun_app.home_cd_label.hide()
    mun_app.settings.toJSON

def onGapClicked(mun_app):
    mun_app.settings.committee_type = 'GAP'
    mun_app.cd_label.hide()
    mun_app.cd_field.hide()
    mun_app.home_cd_label.hide()

    mun_app.settings.toJSON

def onSaveClicked(mun_app):
    mun_app.settings.conference_name = mun_app.conference_title_field.text().strip()
    mun_app.settings.committee_name = mun_app.committee_title_field.text().strip()
    mun_app.settings.chair_name = mun_app.chair_field.text().strip()
    mun_app.settings.co_chair_name = mun_app.co_chair_field.text().strip()
    if(mun_app.crisis_button.isChecked()):
        mun_app.settings.committee_type = 'Crisis'
        mun_app.settings.crisis_director_name = mun_app.cd_field.text().strip()
    elif(mun_app.ga_button.isChecked()):
        mun_app.settings.crisis_director_name = ''
        mun_app.settings.committee_type = 'GA'
    else:
        mun_app.settings.crisis_director_name = ''
        mun_app.settings.committee_type = 'GAP'
    mun_app.welcome_to_conference_label.setText(
        'Welcome to ' + mun_app.settings.conference_name + '!')

    mun_app.home_committee_label.setText(
        'Committee: ' + mun_app.settings.committee_name)
    mun_app.home_chair_label.setText('Chair: ' + mun_app.settings.chair_name)
    mun_app.home_co_label.setText('Co-Chair: ' + mun_app.settings.co_chair_name)
    if(mun_app.settings.committee_type.lower() == 'crisis'):
        mun_app.home_cd_label.setText(
            'Crisis Director: ' + mun_app.settings.crisis_director_name)
        mun_app.home_cd_label.show()
    else:
        mun_app.home_cd_label.hide()
    mun_app.settings.toJSON()

# Points and Motions Button Functions
def resetMotions(mun_app):
    for view in mun_app.motion_views:
        view.setParent(None)
    addMotionView(mun_app)

def addMotionView(mun_app):
    motion_options = resource_path('motion_options.ui')
    mun_app.motion_views.append(uic.loadUi(motion_options))

    mun_app.motion_views[-1].delegates_combo_box.setEditable(True)
    mun_app.motion_views[-1].delegates_combo_box.lineEdit().setReadOnly(True)
    mun_app.motion_views[-1].delegates_combo_box.lineEdit(
    ).setAlignment(QtCore.Qt.AlignCenter)
    
    mun_app.points_motions_layout.addWidget(mun_app.motion_views[-1])
    
    
    mun_app.motion_views[-1].start_motion_button.clicked.connect(
        lambda _, b=mun_app.motion_views[-1]: startCaucusFromMotions(mun_app,b))
    mun_app.motion_views[-1].delete_motion_button.clicked.connect(
        lambda _, b=mun_app.motion_views[-1]: removeMotionView(mun_app,b)
    )

def removeMotionView(mun_app, b):
    b.hide()

def startCaucusFromMotions(mun_app, b):
    motioned_by = b.delegates_combo_box.currentData()
    if(motioned_by == None):
        motioned_by = Delegate('You need to add delegates first')
    if(b.mod_check_box.isChecked()):
        mun_app.caucus = ModeratedCaucus(b.doubleSpinBox.value(), b.spinBox.value(
        ), b.topic_line_edit.text().strip(), motioned_by, b.first_check_box.isChecked())
        for i in reversed(range(mun_app.speaker_list_layout.count())):
            mun_app.speaker_list_layout.itemAt(i).widget().setParent(None)
        setUpMod(mun_app,mun_app.caucus.duration,
                        mun_app.caucus.speaking_time, mun_app.caucus.topic)
    elif(b.unmod_check_box.isChecked()):
        mun_app.defualt_unmod_time_value = int(b.doubleSpinBox.value() * 60)
        resetTimer(mun_app,'unmod')
        mun_app.content_pane.setCurrentIndex(6)

def addItemComboBox(mun_app, delegate):
    for view in mun_app.motion_views:
        view.delegates_combo_box.addItem(delegate.title, delegate)
        view.delegates_combo_box.setItemData(1, 1, Qt.UserRole)

def removeItemComboBox(mun_app, name):
    for view in mun_app.motion_views:
        for i in range(view.delegates_combo_box.count()):
            if(view.delegates_combo_box.itemText(i) == name):
                view.delegates_combo_box.removeItem(i)

def addModPressed(mun_app):
    mun_app.motioned_by_combo_box.clear()
    for delegate in mun_app.settings.delegates:
        mun_app.motioned_by_combo_box.addItem(delegate.title, delegate)

    mun_app.content_pane.setCurrentIndex(mun_app.ADD_MOD_INDEX)

def addModeratedCaucus(mun_app):
    motioned_by = mun_app.motioned_by_combo_box.currentData()
    if(motioned_by == None):
        motioned_by = Delegate('You need to add delegates first')

    mun_app.caucus = ModeratedCaucus(mun_app.duration_spin_box.value(
    ), mun_app.speaking_time_spin_box.value(), mun_app.add_mod_topic_field.text().strip(), motioned_by, mun_app.first_speech_button.isChecked())

    for i in reversed(range(mun_app.speaker_list_layout.count())):
        mun_app.speaker_list_layout.itemAt(i).widget().setParent(None)
    setUpMod(mun_app,mun_app.caucus.duration,
                    mun_app.caucus.speaking_time, mun_app.caucus.topic)
    updateData(mun_app)

def setUpMod(mun_app, duration, speaking_time, topic):
    mun_app.speaker_list_layout.setAlignment(Qt.AlignTop)
    if (duration * 60 / speaking_time).is_integer():
        num_speakers = (duration * 60 / speaking_time)
    else:
        return
    for i in range(int(num_speakers)):
        speaker_view = resource_path('speaker_view.ui')
        speaker_view = uic.loadUi(speaker_view)
       
        speaker_view.add_speaker_button.clicked.connect(
            lambda _, b=speaker_view: onAddSpeakerClicked(mun_app,b))
        speaker_view.cancel_speaker_button.clicked.connect(
            lambda _, b=speaker_view: onCancelSpeakerClicked(mun_app,b))
        speaker_view.confirm_speaker_button.clicked.connect(
            lambda _, b=speaker_view: onConfirmSpeakerClicked(mun_app,b))

        for delegate in mun_app.settings.delegates:
            speaker_view.add_speaker_combo_box.addItem(
                delegate.title, delegate)

        speaker_view.speaker_number_label.setText(str(i+1))
        
        if(mun_app.caucus.is_first_speaker and i == 0):
            speaker_view.speaker_name_label.setText(
                mun_app.caucus.motioned_by.title)
        elif(not mun_app.caucus.is_first_speaker and i == num_speakers - 1):
            speaker_view.speaker_name_label.setText(
                mun_app.caucus.motioned_by.title)

        mun_app.speaker_list_layout.addWidget(speaker_view)

    mun_app.caucus.motioned_by.times_called_on += 1
    updateData(mun_app)
    mun_app.mod_info_label.setText(
        str(duration) + ' minute ' + str(speaking_time) + ' second caucus on ' + topic)
    mun_app.countdown_value_mod = speaking_time
    mun_app.content_pane.setCurrentIndex(4)
    if(mun_app.countdown_value_mod > 99):
        mun_app.countdown_timer.setDigitCount(4)
    elif(mun_app.countdown_value_mod >= 10):
        mun_app.countdown_timer.setDigitCount(4)
    else:
        mun_app.countdown_timer.setDigitCount(4)
    mun_app.countdown_timer.display(getTime(mun_app.countdown_value_mod))

def onAddSpeakerClicked(mun_app, b):
    b.setCurrentIndex(1)

def onCancelSpeakerClicked(mun_app, b):
    b.setCurrentIndex(0)

def addExtClicked(mun_app):
    for delegate in mun_app.settings.delegates:
        mun_app.ext_combo_box.addItem(delegate.title, delegate)
        mun_app.add_ext_stack.setCurrentIndex(1)

def addExtension(mun_app):
    duration = mun_app.ext_spin_box.value()
    mun_app.speaker_list_layout.setAlignment(Qt.AlignTop)
    mun_app.ext_combo_box.currentData().times_called_on += 1
    updateData(mun_app)
    if((duration * 60 / mun_app.caucus.speaking_time).is_integer() and not duration == 0):
        num_extra_speakers = (duration * 60 / mun_app.caucus.speaking_time)
        for i in range(int(num_extra_speakers) + 1):
            speaker_view = resource_path('speaker_view.ui')
            speaker_view = uic.loadUi(speaker_view)
            if i == 0:
                speaker_view.setCurrentIndex(2)

            speaker_view.add_speaker_button.clicked.connect(
                lambda _, b=speaker_view: onAddSpeakerClicked(mun_app,b))
            speaker_view.cancel_speaker_button.clicked.connect(
                lambda _, b=speaker_view: onCancelSpeakerClicked(mun_app,b))
            speaker_view.confirm_speaker_button.clicked.connect(
                lambda _, b=speaker_view: onConfirmSpeakerClicked(mun_app,b))

            for delegate in mun_app.settings.delegates:
                speaker_view.add_speaker_combo_box.addItem(
                    delegate.title, delegate)
            num_prev = int(mun_app.caucus.duration * 60 /
                            mun_app.caucus.speaking_time)
            speaker_view.speaker_number_label.setText(str(i+num_prev))
            if(mun_app.ext_first.isChecked() and i == 1):
                speaker_view.speaker_name_label.setText(
                    mun_app.ext_combo_box.currentData().title)
            elif(not mun_app.ext_first.isChecked() and i == num_extra_speakers):
                speaker_view.speaker_name_label.setText(
                    mun_app.ext_combo_box.currentData().title)

            mun_app.speaker_list_layout.addWidget(speaker_view)
        mun_app.add_ext_stack.setCurrentIndex(0)

def onConfirmSpeakerClicked(mun_app, b):
    delegate = b.add_speaker_combo_box.currentData()
    b.speaker_name_label.setText(delegate.title)
    delegate.times_called_on += 1
    updateData(mun_app)
    mun_app.settings.toJSON()
    updateData(mun_app)
    b.setCurrentIndex(0)

def startTimer(mun_app, mode):
    mun_app.timer_state = True
    if(mode == 'mod'):
        for tick in range(mun_app.countdown_value_mod, 0, -1):
            mun_app.countdown_timer.setDigitCount(
                len(getTime(mun_app.countdown_value_mod - 1)))
            if(mun_app.timer_state):
                mun_app.countdown_value_mod = mun_app.countdown_value_mod - 1
                mun_app.countdown_timer.display(
                    getTime(mun_app.countdown_value_mod))
                mun_app.start_timer_mod.setEnabled(not tick)
                start = time.time()
                while time.time() - start < 1:
                    mun_app.app.processEvents()
                    time.sleep(0.02)
    else:
        for tick in range(mun_app.countdown_value_unmod, 0, -1):
            mun_app.unmod_timer.setDigitCount(
                len(getTime(mun_app.countdown_value_unmod)))
            if(mun_app.timer_state):
                mun_app.countdown_value_unmod = mun_app.countdown_value_unmod - 1
                mun_app.unmod_timer.display(
                    getTime(mun_app.countdown_value_unmod))
                mun_app.unmod_timer_start_button.setEnabled(not tick)
                start = time.time()
                while time.time() - start < 1:
                    mun_app.app.processEvents()
                    time.sleep(0.02)

def pauseTimer(mun_app, mode):
    if(mun_app.timer_state):
        mun_app.timer_state = False
    else:
        mun_app.timer_state = True
        startTimer(mun_app,mode)

def resetTimer(mun_app, mode):
    if(mun_app.timer_state):
        pauseTimer(mun_app,mode)

    mun_app.timer_state = False
    if(mode == 'mod'):
        mun_app.countdown_value_mod = mun_app.caucus.speaking_time
        mun_app.countdown_timer.setDigitCount(
            len(getTime(mun_app.countdown_value_mod)))
        mun_app.countdown_timer.display(getTime(mun_app.countdown_value_mod))
        mun_app.start_timer_mod.setEnabled(True)
    else:
        mun_app.countdown_value_unmod = mun_app.defualt_unmod_time_value
        mun_app.unmod_timer.setDigitCount(
            len(getTime(mun_app.countdown_value_unmod)))
        mun_app.unmod_timer.display(getTime(mun_app.countdown_value_unmod))
        mun_app.unmod_timer_start_button.setEnabled(True)

# Unmod
def setUnmod(mun_app, seconds):
    mun_app.defualt_unmod_time_value = seconds
    mun_app.countdown_value_unmod = mun_app.defualt_unmod_time_value
    resetTimer(mun_app,'unmod') 
    mun_app.add_unmod_widget.setCurrentIndex(0)


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)
