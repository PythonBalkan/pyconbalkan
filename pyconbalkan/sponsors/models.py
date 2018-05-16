from django.db import models
from django.core.exceptions import ValidationError
from djchoices import DjangoChoices, ChoiceItem
from pyconbalkan.core.models import ActiveModel


class SponsorshipLevel(DjangoChoices):
    keystone = ChoiceItem('Keystone')
    platinum = ChoiceItem('Platinum')
    gold = ChoiceItem('Gold')
    silver = ChoiceItem('Silver')
    partner = ChoiceItem('Partner')


LIMITS = {
    SponsorshipLevel.keystone: 1,
    SponsorshipLevel.platinum: 6,
    SponsorshipLevel.gold: 10,
    SponsorshipLevel.silver: 15,
    SponsorshipLevel.partner: 10e6
}


class Sponsor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    level = models.CharField(max_length=16, choices=SponsorshipLevel.choices)
    logo = models.ImageField(
        upload_to='static/img/sponsors', null=True, blank=True
    )

    def __str__(self):
        return f'Sponsor [{self.name}]'

    __repr__ = __str__

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        count = Sponsor.objects.filter(level=self.level).count()
        if count >= LIMITS[self.level]:
            raise ValidationError(
                f'Sponsorship level {self.level} allows only '
                f'{LIMITS[self.level]} sponsors'
            )
        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)


class PackageOption(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)


class SponsorshipPackage(ActiveModel):
    name = models.CharField(max_length=256)
    limit = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    options = models.ManyToManyField('PackageOption', through='SponsorshipPackageOptions')


class SponsorshipPackageOptions(models.Model):
    package = models.ForeignKey(SponsorshipPackage, on_delete=models.CASCADE)
    option = models.ForeignKey(PackageOption, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('package', 'option')
