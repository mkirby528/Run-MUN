from gui_functionality import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sys
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


def setUpHomePage(mun_app):

    mun_app.welcome_to_conference_label.setText(
        'Welcome to ' + mun_app.settings.conference_name + '!')
    mun_app.home_committee_label.setText(
        'Committee: ' + mun_app.settings.committee_name)
    mun_app.home_chair_label.setText('Chair: ' + mun_app.settings.chair_name)
    mun_app.home_co_label.setText(
        'Co-Chair: ' + mun_app.settings.co_chair_name)

    mun_app.home_delegates_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.DELEGATES_INDEX))
    mun_app.home_pm_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.POINTS_MOTIONS_INDEX))
    mun_app.home_mod_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.MOD_INDEX))
    mun_app.home_unmod_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.UNMOD_INDEX))
    mun_app.home_stats_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.DATA_INDEX))
    mun_app.home_settings_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.SETTINGS_INDEX))
    if(mun_app.settings.committee_type.lower() == 'crisis'):
        mun_app.home_cd_label.setText(
            'Crisis Director: ' + mun_app.settings.crisis_director_name)
        mun_app.home_cd_label.show()
    else:
        mun_app.home_cd_label.hide()


def setUpSidebar(mun_app):
    mun_app.home_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.HOME_INDEX))
    mun_app.delegates_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.DELEGATES_INDEX))
    mun_app.add_delegate_button.clicked.connect(lambda: onAddDelButtonClicked(mun_app))
    mun_app.points_motions_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.POINTS_MOTIONS_INDEX))
    mun_app.moderated_caucus_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.MOD_INDEX))
    mun_app.add_mod_caucus_button.clicked.connect(
        lambda: addModPressed(mun_app))
    mun_app.unmod_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.UNMOD_INDEX))
    mun_app.stats_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.DATA_INDEX))
    mun_app.settings_button.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.SETTINGS_INDEX))


def setUpSettingsPage(mun_app):

    mun_app.crisis_button.clicked.connect(lambda: onCrisisClicked(mun_app))
    mun_app.ga_button.clicked.connect(lambda: onGaClicked(mun_app))
    mun_app.gap_button.clicked.connect(lambda: onGapClicked(mun_app))
    mun_app.save_button.clicked.connect(lambda: onSaveClicked(mun_app))

    # Fill fields with current data
    mun_app.conference_title_field.setText(mun_app.settings.conference_name)
    mun_app.committee_title_field.setText(mun_app.settings.committee_name)
    mun_app.chair_field.setText(mun_app.settings.chair_name)
    mun_app.co_chair_field.setText(mun_app.settings.co_chair_name)
    mun_app.cd_field.setText(mun_app.settings.crisis_director_name)
    if(mun_app.settings.committee_type.lower() == 'crisis'):
        mun_app.home_cd_label.setText(
            'Crisis Director: ' + mun_app.settings.crisis_director_name)
        mun_app.home_cd_label.show()

    else:
        mun_app.home_cd_label.hide()


def setUpDelegatesPages(mun_app):

    mun_app.export_attendence.clicked.connect(lambda: exportAttendence(mun_app))
    mun_app.order_delegates_button.clicked.connect(lambda:onOrderDelegates(mun_app))
    mun_app.remove_all_del_button.clicked.connect(
        lambda: mun_app.rm_all_widget.setCurrentIndex(1))
    mun_app.cancel_rm_button.clicked.connect(
        lambda: mun_app.rm_all_widget.setCurrentIndex(0))
    mun_app.confirm_rm_button.clicked.connect(lambda: removeAllDelegates(mun_app))

    mun_app.cancel_button.clicked.connect(lambda:onCancelButtonPressed(mun_app))
    mun_app.confirm_add_button.clicked.connect(
        lambda: onConfirmAddDelegatePressed(mun_app))

    update_del_info_label(mun_app)

    for i in range(len(mun_app.settings.delegates)):
        delegate_ui = resource_path('delegate_view.ui')

        del_view = uic.loadUi(delegate_ui)
        mun_app.dels_layout.setAlignment(Qt.AlignTop)

        delegate = mun_app.settings.delegates[i]

        if(delegate.isPresent):
            del_view.present_button.setChecked(True)
            del_view.absent_button.setChecked(False)
        else:
            del_view.present_button.setChecked(False)
            del_view.absent_button.setChecked(True)

        del_view.delegate_name_label.setText(delegate.title)
        del_view.delete_delegate_button.clicked.connect(
            lambda _, b=del_view: deleteDelegate(mun_app,b))

        del_view.present_button.clicked.connect(
            lambda _, b=del_view: onPresentClicked(mun_app,b))
        del_view.absent_button.clicked.connect(
            lambda _, b=del_view: onAbsentClicked(mun_app,b))

        mun_app.dels_layout.addWidget(del_view)


def setUpPointsMotionsPage(mun_app):
    mun_app.motion_views = []
    mun_app.points_motions_layout.setAlignment(Qt.AlignTop)
    mun_app.add_motion_button.clicked.connect(lambda: addMotionView(mun_app))
    mun_app.reset_motions_button.clicked.connect(lambda:resetMotions(mun_app))
    addMotionView(mun_app)



def setUpModPages(mun_app):
    mun_app.cancel_button_mod.clicked.connect(
        lambda: mun_app.content_pane.setCurrentIndex(mun_app.MOD_INDEX))
    mun_app.confirm_add_button_mod.clicked.connect(
        lambda:  addModeratedCaucus(mun_app))

    mun_app.start_timer_mod.clicked.connect(lambda: startTimer(mun_app,'mod'))
    mun_app.pause_timer_mod.clicked.connect(lambda: pauseTimer(mun_app,'mod'))
    mun_app.reset_timer_mod.clicked.connect(lambda: resetTimer(mun_app,'mod'))
    mun_app.add_ext_button.clicked.connect(lambda: addExtClicked(mun_app))
    mun_app.cancel_add_ext.clicked.connect(lambda: mun_app.add_ext_stack.setCurrentIndex(0))
    mun_app.confirm_add_ext.clicked.connect(lambda: addExtension(mun_app))

def setUpUnmodPage(mun_app):
    mun_app.unmod_timer.setDigitCount(len(getTime(mun_app.countdown_value_mod)))
    mun_app.unmod_timer.display(getTime(mun_app.countdown_value_unmod))

    mun_app.unmod_timer_start_button.clicked.connect(
        lambda: startTimer(mun_app,'unmod'))
    mun_app.unmod_timer_pause_button.clicked.connect(
        lambda: pauseTimer(mun_app,'unmod'))
    mun_app.unmod_timer_reset_button.clicked.connect(
        lambda: resetTimer(mun_app,'unmod'))
    mun_app.add_unmod_button.clicked.connect(
        lambda: mun_app.add_unmod_widget.setCurrentIndex(1))
    mun_app.cancel_set_unmod.clicked.connect(
        lambda: mun_app.add_unmod_widget.setCurrentIndex(0))
    mun_app.confirm_set_unmod.clicked.connect(lambda:  setUnmod(mun_app,
        mun_app.set_unmod_min_spinbox.value() * 60 + mun_app.set_unmod_sec_spinbox.value()))

def setUpStatsPage(mun_app):
    mun_app.figure = Figure()
    mun_app.canvas = FigureCanvas(mun_app.figure)

    mun_app.ax = mun_app.figure.add_subplot(111)
    mun_app.figure.patch.set_facecolor('#4B9CD3')
    mun_app.ax.set_facecolor("#13294B")
    mun_app.stats_layout.addWidget(mun_app.canvas)
    updateData(mun_app)

    mun_app.reset_data_button.clicked.connect(lambda: mun_app.reset_data_widget.setCurrentIndex(1))
    mun_app.cancel_rm_button2.clicked.connect(lambda: mun_app.reset_data_widget.setCurrentIndex(0))
    mun_app.confirm_rm_button2.clicked.connect(lambda:reset_data(mun_app))