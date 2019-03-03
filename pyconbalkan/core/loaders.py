from os import path

from django.template import TemplateDoesNotExist
from django.template.loaders.app_directories import Loader

from pyconbalkan.conference.context import singleton


class PyconLoader(Loader):
    def get_template(self, template_name, skip=None):
        if not hasattr(singleton, "conference"):
            raise TemplateDoesNotExist(
                "Conference object not be found in context, skipping."
            )
        template_basename = "{:d}_{}".format(
            singleton.conference.year, path.basename(template_name)
        )
        template_name = path.join(path.dirname(template_name), template_basename)

        return super(PyconLoader, self).get_template(template_name, skip=None)
