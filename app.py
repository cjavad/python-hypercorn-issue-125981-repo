import logging
from pathlib import Path
from typing import Callable, Awaitable, Dict, Any
from hypercorn.typing import ASGIFramework
from hypercorn.config import Config
from hypercorn.asyncio import serve

async def app(scope, receive, send):
    if scope["type"] == "http" and scope["path"] == "/":
        response_body = b'<link rel="icon" href="data:,"> Hello world!'
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [
                (b"content-type", b"text/plain"),
            ],
        })
        await send({
            "type": "http.response.body",
            "body": response_body,
        })

CERTS_DIR = Path(__file__).resolve().parent / "certs"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    config = Config()
    config.bind = ["0.0.0.0:3000"]
    config.certfile = str(CERTS_DIR / "ssl_cert.pem")
    config.keyfile = str(CERTS_DIR / "ssl_key.pem")
    config.loglevel = "info"
    config.accesslog = "-"
    import asyncio
    asyncio.run(serve(app, config))

