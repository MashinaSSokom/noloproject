from .settings import *


def secret_front(request,  *args, **kwargs):
    request['secret'] = SECRET


BASE_MIDDLEWARE = [secret_front]

