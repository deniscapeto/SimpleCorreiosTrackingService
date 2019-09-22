from scts.tracking.models import TrackingCode
from django.core import serializers

def ExtractTrackingEvents(html):

    trackingCodes = []

    trackingCode = TrackingCode('01/02/2019', 'produto postado')

    trackingCodes.append(trackingCode)

    trackingCode.save()

    result = serializers.serialize('json', trackingCodes)

    return result