import asyncio
import aiohttp
from aiohttp import web
from collections import deque
import urllib.parse
import time

expressions = deque()

no_requests = 0
printCount = 0
start_time = 0


# I am taking the assumption that user triggers the bulk requests from their test application instead of sending a
# bulk expressions in a single querry and implementing a bulk enquiry is not that hard second assumption is that
# since we are not sending any reply back to the user I am decoupling the user and their execution data This is the
# main handler which handles the incomming requests to the app and and also triggers when even a end statement is
# received
async def handle(request):
    global expressions
    global no_requests
    global start_time
    data = await request.text()
    expressions.append(data)
    if data == "count":
        print("printing the count::", printCount)
        return web.Response(text=f'count {printCount}')
    if data == "end":
        no_requests += 1
    if no_requests > 0 and start_time - time.time() < 1:
        start_time = time.time()
        asyncio.create_task(main())

        return web.Response(text='Thanks for reaching out')

    return web.Response(text='noted!')


# This is the fetch funciton to actually fetch the external api
async def fetch(session, expr):
    encoded_expr = urllib.parse.quote(expr)
    url = f"http://api.mathjs.org/v4/?expr={encoded_expr}"
    async with session.get(url) as response:
        return expr, await response.text()


app = web.Application()
app.router.add_post('/expressions', handle)


# This main funciton has logic to trigger only 50 requests per second and only executes if there is still a pending
# user request after he has given a end statement
async def main():
    global printCount
    global expressions
    global no_requests
    async with aiohttp.ClientSession() as session:
        global start_time
        tasks = []
        req = 0
        start_time = time.time()
        while (req < 50 and expressions):
            t = expressions.popleft()
            if t == 'end':
                no_requests -= 1
                break
            tasks.append(fetch(session, t))
            req += 1
        responses = await asyncio.gather(*tasks)
        for expr, i in responses:
            printCount += 1
            print(f"{i} is the answer for {expr}")
        if no_requests > 0 and start_time - time.time() < 1:
            start_time = time.time()
            asyncio.create_task(main())


if __name__ == '__main__':
    web.run_app(app)
