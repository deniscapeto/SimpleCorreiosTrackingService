from django.db import models

class TrackingCode(models.Model):
    date = models.CharField(max_length=500)
    description = models.CharField(max_length=300)
    
    def __init__(self, date, description):
        super(TrackingCode, self).__init__()
        self.date = date
        self.description = description

    def serialize(self):    
        return {
            "date" : self.date,
            "description" : self.description
         }

    class Meta:
        db_table = 'tracking'
        app_label = 'tracking'
        managed = True