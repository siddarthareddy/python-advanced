from aiohttp import web

# describes routes by decorators
routes = web.RouteTableDef()

# for localhost:8080/ -->
# Async Server in Python 3.7
@routes.get('/')
async def handler(request):
    return web.Response(text='Async Server in Python 3.7')


# for localhost:8080/Java -->>
# The programming language entered was: Java
@routes.get('/{language}')
async def return_language(request):
    lang = request.match_info.get('language', '')
    return web.Response(text=f'The programming language entered was: {lang}')

# another way to pass info with url is to pass key-value pairs
# for localhost:8080/Java?other=what -->>
# The programming language entered was: Java
# Other info: what
@routes.get('/ok/{language}')
async def return_language(request):
    lang = request.match_info.get('language', '')
    other_info = request.rel_url.query.get('other', '')
    return web.Response(text=f'''
    The programming language entered was: {lang}
    Other info: {other_info}
    ''')


@routes.post('/add_lang')
async def add_lang(request):
    print("hello")
    data = await request.post()
    lang = data.get('language')
    return web.Response(text=f'{lang} was added to database')


async def initialization():
    app = web.Application()
    app.add_routes(routes)
    return app


# app = web.Application()
# # this way async functions can be plugged in to the web application
# app.add_routes([web.get('/', handler)])
# # alternative way to register routes is to use decorators and add them
# at the start of handler coroutines
# web.run_app(app)
web.run_app(initialization())
