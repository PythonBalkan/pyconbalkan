import os
from time import time

from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage


class UniqueNameMixin(object):
    def get_timestamped_name(self, name, max_length=None):
        """
        Return a filename that's free on the target storage system and
        available for new content to be written to.
        """
        milisecond = str(int(round(time() * 1000)))
        extension = name.split('.')[-1].strip().lower() if '.' in name else 'none'

        return '{}.{}'.format(milisecond, extension)

    def generate_filename(self, filename):
        """
        Validate the filename by calling get_valid_name() and return a filename
        to be passed to the save() method.
        """
        # `filename` may include a path as returned by FileField.upload_to.
        dirname, filename = os.path.split(filename)
        return os.path.normpath(os.path.join(dirname, self.get_timestamped_name(filename)))


class S3Storage(UniqueNameMixin, S3Boto3Storage):
    bucket_name = "pyconbalkan-us"


class LocalStorage(UniqueNameMixin, FileSystemStorage):
    def generate_filename(self, filename):
        filename = os.path.join("static", filename)
        return super().generate_filename(filename)

