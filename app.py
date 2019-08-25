from aiohttp import web
import json

routes = web.RouteTableDef()

@routes.get('/')
async def handle(request):
    response_obj = { 'status': 'success' }
    return web.Response(text=json.dumps(response_obj),status=200)

app = web.Application()
# app.router.add_get('/',handle)

app.add_routes(routes)

web.run_app(app)

