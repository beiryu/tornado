import asyncio
import tornado.options
import tornado.httpserver
from storefront.asgi import Application

async def main():
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())