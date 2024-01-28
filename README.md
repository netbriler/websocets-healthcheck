# Websockets Healthcheck

Environment variables:

- `WEB_SOCKETS_URL`: The URL of the websocket server. Defaults to `ws://localhost:3001/healthz`.

## Usage

```bash
docker run --rm -e WEB_SOCKETS_URL=ws://localhost:3001/healthz briler/websockets-healthcheck:latest
```