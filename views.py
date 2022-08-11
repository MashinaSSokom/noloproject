from nolo.templator import Templator


def main_view(request):
    print(request)
    return {
        'code': '200 OK',
        'body': Templator.render(template_name='pages/index.html',
                                 data=request.get('USERNAME', None))
    }


def contacts_view(request):
    print(request)
    return {
        'code': '200 OK',
        'body': Templator.render(template_name='pages/contacts.html',
                                 data=request.get('USERNAME', None))
    }


def login_view(request):
    print(request)
    return {
        'code': '200 OK',
        'body': Templator.render(template_name='pages/login.html',
                                 data=request.get('data', None))
    }


def registration_view(request):
    print(request)
    return {
        'code': '200 OK',
        'body': Templator.render(template_name='pages/registration.html',
                                 data=request.get('data', None))
    }
