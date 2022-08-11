import os
from jinja2 import Template


class Templator:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    @staticmethod
    def render(template_name, template_dir='templates', **kwargs):
        file_path = os.path.join(template_dir, template_name)
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            template = Template(f.read())

        return template.render(**kwargs)
