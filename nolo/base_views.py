from .templator import Templator


def not_found_view(request):
    return {'status': '404 NOT FOUND', 'body': Templator.render(template_name='not_found.html',
                                                                template_dir='nolo/base_templates',
                                                                data=request.get('data', None))}
