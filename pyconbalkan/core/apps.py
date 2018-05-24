from django.apps import AppConfig
from django.contrib.staticfiles.apps import StaticFilesConfig


class CoreConfig(AppConfig):
    name = 'core'


class ProjectStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = ['src', 'dst']
