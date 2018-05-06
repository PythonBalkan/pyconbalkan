from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class ActiveModel(models.Model):
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class SingleActiveModel(ActiveModel):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.active:
            # select all other active items
            qs = type(self).objects.filter(active=True)
            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            # and deactive them
            qs.update(active=False)

        super(SingleActiveModel, self).save(*args, **kwargs)