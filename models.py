
class TrackingCode(object):
    
    def __init__(self, date, description):
        self.date = date
        self.description = description

    def serialize(self):    
        return {
            "date" : self.date,
            "description" : self.description
         }