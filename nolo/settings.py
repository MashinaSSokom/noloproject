import os

SECRET = 'yoursecretkey'
HOST = 'localhost'
PORT = '8083'

STATIC_DIR = '/static/'
STATIC_DIR_PATH = os.path.join(os.path.dirname(__file__), f'..{STATIC_DIR}')
