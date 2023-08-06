import tools
import asyncio
import requests

import time
import os, sys

SCRIPT_DIR = "."
if __name__ == "__main__":
    SCRIPT_DIR = os.path.dirname(
        os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
    )
    SCRIPT_DIR = os.path.join(SCRIPT_DIR, "..")
    sys.path.insert(0, os.path.normpath(SCRIPT_DIR))


async def test():
    for i in range(0, 3):

        async for chunk in tools.generate_random_bytes(
            size_bytes=32, chunk_size_bytes=32, seed=1234
        ):
            print(chunk)


asyncio.run(test())
asyncio.run(test())


from shittywebserver.main import run_shitty_webserver

proc = run_shitty_webserver(run_in_subprocess=True, port=8888)
time.sleep(1)
for i in range(0, 3):
    print(
        requests.get(
            "http://localhost:8888/v1/download/static-content-static-etag?size_bytes=32"
        ).content
    )
proc.terminate()
proc.join()
