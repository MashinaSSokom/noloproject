def set_username(request, *args, **kwargs):
    request['USERNAME'] = args[0]['USERNAME']
