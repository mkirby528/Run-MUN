import jsonpickle, simplejson
from enum import Enum
import os,sys
from PyQt5 import QtCore, QtGui, uic,QtWidgets

class Settings(object):



    def __init__(self):
            self.conference_name = 'Default Conference Name'
            self.committee_name = 'Default Committee Name'
            self.chair_name = 'Default Chair Name'
            self.co_chair_name = 'Default Co-Chair Name'
            self.committee_type = 'Crisis'
            self.total_present_delegates = 0
            self.delegates=[]
            self.crisis_director_name  ='Defualt CD Name'
            self.toJSON()
      

    
    def toJSON(self):
       
        json = resource_path('config.json')

        with open(json,'w') as file:
            jsonpickle.set_preferred_backend('simplejson')
            file.write(jsonpickle.encode(self))
            file.close()

class Delegate(object):

    def __init__(self,title='Default Name'):
        self.title = title
        self.isPresent = True
        self.times_called_on = 0


    
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)
