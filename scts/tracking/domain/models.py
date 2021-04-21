from django.db import models


class TrackingEvent(models.Model):
    code = models.CharField(max_length=30)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500)

    def __init__(self, code, date, location, description):
        super(TrackingEvent, self).__init__()
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

    class Meta:
        db_table = 'tracking_event'
        app_label = 'tracking'
        managed = True
