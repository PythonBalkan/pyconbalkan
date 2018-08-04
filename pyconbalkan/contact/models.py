from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        contact_str = '{} | {}'.format(self.name, self.email)
        if self.company:
            return '{} | {}'.format(contact_str, self.company)
        return contact_str

