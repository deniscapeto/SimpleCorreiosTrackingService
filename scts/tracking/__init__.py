class Container:

    container = {}

    @classmethod
    def add(cls, key, value):
        cls.container[key] = value

    @classmethod
    def get(cls, key):
        return cls.container[key]


def bootstrap():
    """
    THIS IS A TEMPORARY SOLUTION, BEFORE IMPLEMENTING
    THE USE OF A LIB TO INJECT DEPENDENCIES
    """

    from scts.tracking.application.services import GetTrackingEventsService
    from scts.tracking.domain.repositories import TrackingEventRepository
    from scts.tracking.infrastructure.django_repositories import DjangoTrackingEventRepository

    container = Container

    container.add(TrackingEventRepository, DjangoTrackingEventRepository())
    container.add(GetTrackingEventsService, GetTrackingEventsService(
            container.get(TrackingEventRepository)
        )
    )
