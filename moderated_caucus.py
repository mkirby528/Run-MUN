import time 

class ModeratedCaucus():

    def __init__(self, duration, speaking_time, window,app, topic='General Discussion'):
        self.timer_state = False
        self.app = app
        self.window = window
        self.duration = duration
        self.speaking_time = speaking_time
        self.topic = topic
        self.countdown_timer_value = speaking_time
        self.window.start_timer_mod.clicked.connect(lambda: self.startTimer(self.countdown_timer_value))
        self.window.pause_timer_mod.clicked.connect(self.pauseTimer)
        speakers = []

    def startCauscus(self):
        self.window.content_pane.setCurrentIndex(4)
        if(self.countdown_timer_value > 99):
            self.window.countdown_timer.setDigitCount(3)
        elif(self.countdown_timer_value >= 10):
            self.window.countdown_timer.setDigitCount(2)
        else:
            self.window.countdown_timer.setDigitCount(1)
        self.window.countdown_timer.display(self.speaking_time)
        self.window.mod_info_label.setText(str(self.duration) + ' minute ' + str(
            self.speaking_time) + ' second speaking time on the topic of ' + self.topic)
        self.window.repaint()

    def startTimer(self, seconds=60):
            self.timer_state = True
            self.window.countdown_timer_value = seconds
            for tick in range(self.countdown_timer_value, -1, -1):
                if(self.window.countdown_timer_value > 99):
                    self.window.countdown_timer.setDigitCount(3)
                elif(self.window.countdown_timer_value >= 10):
                    self.window.countdown_timer.setDigitCount(2)
                else:
                    self.window.countdown_timer.setDigitCount(1)
                if(self.timer_state):
                    self.countdown_timer_value = self.countdown_timer_value - 1
                    self.window.countdown_timer.display(self.countdown_timer_value)
                    self.window.start_timer_mod.setEnabled(not tick)
                    start = time.time()
                    while time.time() - start < 1:
                        self.app.processEvents()
                        time.sleep(0.02)

    def pauseTimer(self):
        if(self.timer_state):
            self.timer_state = False
        else:
            self.timer_state = True
            self.startTimer(self.countdown_timer_value)
