"""To create a middleware you use the decorator
`@app.middleware('http')` on top of a function

The middleware function receives:
    - The `request`
    - A function `call_next` that will receive the `request` as a parameter
        - This function will pass the `request` to the corresponding *path* operation
        - Then it returns the `response` generated by the corresponding *path* operation
    - You can then modify further the `response` before returning it.
"""

import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Adds code to be run with the `request`, before any *path operation* receives it.
    And also after the `response` is generated, before returning it.
    For example, add a custom-header `X-Process-Time` containing the time in seconds that it took to process the request and generate a response
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
