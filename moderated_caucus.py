class ModeratedCaucus():

    def __init__(self,duration,speaking_time,window,topic = 'General Discussion'):
        self.window = window
        self.duration = duration
        self.speaking_time =speaking_time
        self.topic  = topic
        speakers = []
    
    def startCauscus(self):
        self.window.content_pane.setCurrentIndex(4)
        self.window.countdown_timer_value = self.speaking_time
        
        if(self.window.countdown_timer_value > 99):
            self.window.countdown_timer.setDigitCount(3)
        elif(self.window.countdown_timer_value >= 10):
            self.window.countdown_timer.setDigitCount(2)
        else:
            self.window.countdown_timer.setDigitCount(1)
        
        self.window.countdown_timer.display(self.speaking_time)
        self.window.mod_info_label.setText(str(self.duration) + ' minute ' + str(self.speaking_time) + ' second speaking time on the topic of ' + self.topic)
        self.window.repaint()
        print(self.speaking_time)
