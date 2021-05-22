from django.db import models


class TrackingEventModel(models.Model):
    code = models.CharField(max_length=35)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, code, date, location, description):
        super(TrackingEventModel, self).__init__()
        self.code = code
        self.date = date
        self.location = location
        self.description = description

    class Meta:
        db_table = 'tracking_event'
        app_label = 'tracking'
        managed = True
