import os.path
from pprint import pprint
from wsgiref.util import setup_testing_defaults

from .base_middlewares import BASE_MIDDLEWARE
from .base_views import not_found_view
from .settings import STATIC_DIR, STATIC_DIR_PATH
from .requests import PostRequests, GetRequests

class Nolo:

    def __init__(self, routes: list, middleware: list = BASE_MIDDLEWARE, not_found_view: object = not_found_view,
                 middleware_kwargs: object = {}):
        self.not_found_view = not_found_view
        self.routes = routes
        self.middleware = middleware
        self.middleware_kwargs = middleware_kwargs

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        # pprint(environ)
        path = environ['PATH_INFO']

        # page_controller
        if path in self.routes:
            view = self.routes[path]
        elif path.startswith(STATIC_DIR):
            filename = path.split('/')[-1]
            print(filename)
            print(STATIC_DIR_PATH)
            static_path = os.path.join(STATIC_DIR_PATH, filename)
            with open(static_path, 'r') as f:
                code, body = [f'200 OK', f.read()]
                start_response(code, [('Content-Type', 'text/css')])
                return [body.encode('utf-8')]
        else:
            view = not_found_view

        request = {}

        method = environ['REQUEST_METHOD']
        if method == 'GET':
            print('get')

        elif method == 'POST':
            data = PostRequests.get_request_data(environ)
            request['data'] = data
            print(f'Получили данные {data}')
        # front_controller
        for layer in self.middleware:
            layer(request, self.middleware_kwargs)

        code, body = view(request).values()

        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
