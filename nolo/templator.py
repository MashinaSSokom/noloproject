import os
from jinja2 import Template, Environment, FileSystemLoader


class Templator:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    @staticmethod
    def render(template_name, template_dir='templates', static_url='/static/', **kwargs):
        file_path = os.path.join(template_dir, template_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            env = Environment()
            env.globals['static'] = static_url
            env.loader = FileSystemLoader(template_dir)
            template = env.get_template(template_name)
        return template.render(**kwargs)
