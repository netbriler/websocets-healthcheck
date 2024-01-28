import os

import websockets
from aiohttp import web

WEB_SOCKETS_URL = os.environ.get('WEB_SOCKETS_URL', 'ws://localhost:3001/healthz')


async def healthz_handler(request):
    try:
        async with websockets.connect(WEB_SOCKETS_URL) as websocket:
            response = await websocket.recv()
            if response != 'ok':
                return web.Response(status=500, text='Not OK\n')
    except Exception:
        return web.Response(status=500, text='Not OK\n')

    return web.Response(status=200, text='OK\n')


async def init_app():
    app = web.Application()
    app.router.add_get('/healthz', healthz_handler)
    return app


if __name__ == '__main__':
    app = init_app()
    web.run_app(app, host='0.0.0.0', port=8080)
