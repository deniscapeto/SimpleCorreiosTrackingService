import inject


def configure(binder):

    from scts.tracking.application.services import GetTrackingEventsService
    from scts.tracking.domain.repositories import TrackingEventRepository
    from tests.unit.tracking.domain.fake_repositories import FakeTrackingEventRepository

    binder.bind(TrackingEventRepository, FakeTrackingEventRepository)
    binder.bind(GetTrackingEventsService, GetTrackingEventsService)


inject.clear_and_configure(configure)
