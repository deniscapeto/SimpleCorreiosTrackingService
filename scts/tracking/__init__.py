def configure(binder):

    from scts.tracking.application.services import GetTrackingEventsService
    from scts.tracking.domain.repositories import TrackingEventRepository
    from scts.tracking.infrastructure.django_repositories import DjangoTrackingEventRepository

    binder.bind(TrackingEventRepository, DjangoTrackingEventRepository)
    binder.bind(GetTrackingEventsService, GetTrackingEventsService)
