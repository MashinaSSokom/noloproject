import datetime
from wsgiref.simple_server import make_server

from nolo.base_middlewares import BASE_MIDDLEWARE as MIDDLEWARE
from nolo.main import Nolo

from router import routes
from middleware import set_username

MIDDLEWARE.extend([set_username])
middleware_kwargs = {
    'USERNAME': 'TestUsername',
}

app = Nolo(routes, middleware=MIDDLEWARE, middleware_kwargs=middleware_kwargs)
with make_server(host='localhost', port=8083, app=app) as httpd:
    print(f'Сервер запущен на порту {8000}')
    httpd.serve_forever()
