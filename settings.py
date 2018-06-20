import jsonpickle
from enum import Enum
import os
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
        with open('config.json','w') as file:
            file.write(jsonpickle.encode(self))
            file.close()

class Delegate(object):

    def __init__(self,title='Default Name'):
        self.title = title
        self.isPresent = True


    