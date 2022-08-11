from wsgiref.util import setup_testing_defaults

from .base_middlewares import BASE_MIDDLEWARE
from .base_views import not_found_view


class Nolo:

    def __init__(self, routes: list, middleware: list = BASE_MIDDLEWARE, not_found_view: object = not_found_view,
                 middleware_kwargs: object = {}):
        self.not_found_view = not_found_view
        self.routes = routes
        self.middleware = middleware
        self.middleware_kwargs = middleware_kwargs

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        path = environ['PATH_INFO']

        # page_controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_view

        # front_controller
        request = {}
        for layer in self.middleware:
            layer(request, self.middleware_kwargs)

        code, body = view(request).values()

        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
