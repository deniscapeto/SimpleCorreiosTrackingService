from views import CorreiosTrackingView

def setup_routes(app):
    app.router.add_view('/tracking/{trackingcode}', CorreiosTrackingView)