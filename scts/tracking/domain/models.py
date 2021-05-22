from datetime import datetime


class TrackingEvent:
    code: str
    date: datetime
    location: str
    description: str

    def __init__(self, code, date, location, description):
        self.code = code
        self.date = date
        self.location = location
        self.description = description

    def as_dict(self):
        return {
            'code': self.code,
            'date': self.date,
            'location': self.location,
            'description': self.description,
         }
