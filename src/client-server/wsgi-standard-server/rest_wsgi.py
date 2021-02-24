"""
Python WSGI - Wes Sever Gateway Interface
PEP 3333

WSGI implementations are in the form of a callable
with signature of environ and start_response
"""

import cgi


def notfound(environ, start_response):
    # http response code, list of name-value tuples that make up headers of response
    start_response('404 Not Found', [('Content', 'text/plain')])
    return [b'404 Not Found']


class PathDispatcher:

    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        print(start_response)
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        print(params)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {k: params.getvalue(k) for k in params}
        handler = self.pathmap.get((method, path), notfound)
        return handler(environ, start_response)

    # allow us to register HTTP methods and paths to python methods
    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function


name_response = """<html>
<body>Hello {name}!</body></html>
"""


def name(environ, start_response):
    start_response('200 OK', [('Content', 'text/html')])
    params = environ['params']
    response = name_response.format(name=params.get('name'))
    yield response.encode('utf-8')


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/name', name)
    httpd = make_server('localhost', 8080, dispatcher)
    httpd.serve_forever()
