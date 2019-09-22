from scts.tracking.views import CorreiosTrackingView

def setup_routes(app):
    app.router.add_view('/tracking/{trackingcode}', CorreiosTrackingView)