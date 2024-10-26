from typing import Callable, Awaitable, Dict, Any
from hypercorn.typing import ASGIFramework
from hypercorn.config import Config
from hypercorn.asyncio import serve

async def app(scope, receive, send):
    if scope["type"] == "http" and scope["path"] == "/":
        response_body = b"Hello world!"
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

if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:3000"]
    config.certfile = "ssl_cert.pem"
    config.keyfile = "ssl_key.pem"
    import asyncio
    asyncio.run(serve(app, config))

