import asyncio


async def handler(reader, writer):
    print("Nova konekcija!")

    writer.write(b"Hello!\n")
    await writer.drain()

    while True:
        l = await reader.readline()
        print(l.decode("utf-8"))


async def main():
    server = await asyncio.start_server(
        handler,  # funkcija koja će zaprimati nove konekcije
        "127.0.0.1",
        8080
    )

    async with server:
        print("Server started")
        await server.serve_forever()


asyncio.run(main())

# nodemon -e py -x python tcp.py
