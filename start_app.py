import datetime
from wsgiref.simple_server import make_server

from nolo.base_middlewares import BASE_MIDDLEWARE as MIDDLEWARE
from nolo.main import Nolo

from router import routes
from middleware import set_username
from settings import PORT, HOST

MIDDLEWARE.extend([set_username])
middleware_kwargs = {
    'USERNAME': 'TestUsername',
}

app = Nolo(routes, middleware=MIDDLEWARE, middleware_kwargs=middleware_kwargs)
with make_server(host=HOST, port=int(PORT), app=app) as httpd:
    print(f'Сервер запущен по адресу http://{HOST}:{PORT}')
    httpd.serve_forever()
