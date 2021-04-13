from aiohttp import web

app = web.Application()

async def hello(request):
    return web.Response(text="Hello, world")


app.add_routes([web.get('/', hello)])

web.run_app(app)