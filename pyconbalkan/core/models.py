from django.db import models


class SingleActiveModel(models.Model):
    active = models.BooleanField(default=False)

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

