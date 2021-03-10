from django.db import models


class TrackingCode(models.Model):
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500)

    def __init__(self, date, location, description):
        super(TrackingCode, self).__init__()
        self.date = date
        self.location = location
        self.description = description

    def as_dict(self):
        return {
            'date': self.date,
            'location': self.location,
            'description': self.description,
         }

    class Meta:
        db_table = 'tracking'
        app_label = 'tracking'
        managed = True
