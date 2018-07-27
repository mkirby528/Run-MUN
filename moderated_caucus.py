import settings

class ModeratedCaucus(object):

    def __init__(self,duration,speaking_time,topic, motioned_by = None, is_first_speaker = True):
        self.duration = duration
        self.speaking_time = speaking_time
        self.topic = topic
        self.motioned_by =  motioned_by
        self.is_first_speaker = is_first_speaker