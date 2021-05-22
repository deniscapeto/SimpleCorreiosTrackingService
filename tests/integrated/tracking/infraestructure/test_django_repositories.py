from asgiref.sync import sync_to_async

from scts.tracking.domain.models import TrackingEvent
from scts.tracking.infrastructure.data_models import TrackingEventModel
from scts.tracking.infrastructure.django_repositories import DjangoTrackingEventRepository
from tests.conftest import tracking_code


async def test_should_add_one_item_in_database():

    tracking_event = TrackingEvent(
        tracking_code,
        '02/03/2021 13:54',
        'SAO PAULO / SP',
        'Objeto entregue ao destinatário'
    )

    repository = DjangoTrackingEventRepository()

    count_before = await get_all_objects()
    await repository.save(tracking_event)
    count_after = await get_all_objects()

    assert count_after - count_before == 1


@sync_to_async
def get_all_objects():
    return TrackingEventModel.objects.count()
