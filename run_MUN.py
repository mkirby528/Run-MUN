import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic

import resources
from gui_functionality import *
from gui_setup import *
from settings import *


class MainWindow(QtWidgets.QWidget):

    def __init__(self, settings, app):
    
        super(MainWindow, self).__init__()
        self.app = app
        munapp_ui = resource_path('mun_app_ui.ui')
        uic.loadUi(munapp_ui, self)
        
        #Class Variable
        self.settings = settings
        self.caucus = ModeratedCaucus(0, 30, 'default topic')
        self.defualt_unmod_time_value = 30
        self.countdown_value_mod = 30
        self.countdown_value_unmod = 30
        self.timer_state = False

        #Content Pane Indexes
        self.HOME_INDEX = 0
        self.DELEGATES_INDEX = 1
        self.ADD_DELEGATE_INDEX =2
        self.POINTS_MOTIONS_INDEX =3
        self.MOD_INDEX = 4
        self.ADD_MOD_INDEX = 5
        self.UNMOD_INDEX = 6
        self.DATA_INDEX = 7
        self.SETTINGS_INDEX = 8
        
      
        
        #Set up GUI
        setUpSidebar(self)
        setUpHomePage(self)
        setUpSettingsPage(self)     
        setUpDelegatesPages(self) 
        setUpPointsMotionsPage(self)  
        setUpModPages(self)
        setUpUnmodPage(self)      
        setUpStatsPage(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

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
    