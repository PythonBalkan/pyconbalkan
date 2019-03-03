from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from markdownx.models import MarkdownxField
from djmoney.models.fields import MoneyField

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
    description = MarkdownxField()
    level = models.CharField(max_length=16, choices=SponsorshipLevel.choices)
    logo = models.ImageField(upload_to="sponsors/logo")

    def __str__(self):
        return f'Sponsor [{ self.name }]'

    __repr__ = __str__

    def save(self, *args, **kwargs):
        if not self.pk:
            count = Sponsor.objects.filter(level=self.level).count()
            if count >= LIMITS[self.level]:
                raise ValidationError(
                    f'Sponsorship level { self.level } allows only '
                    f'{ LIMITS[self.level] } sponsors'
                )
        super(Sponsor, self).save()

PROFIT = 1
NON_PROFIT = 2
ORGANIZATION_CHOICES = (
    (PROFIT, 'Profit Corporation'),
    (NON_PROFIT, 'Foundation / Non profit')
)

class Sponsoring(models.Model):
    organization = models.CharField(max_length=256, null=True, blank=True)
    organization_type = models.IntegerField(choices=ORGANIZATION_CHOICES, default=PROFIT)
    name = models.CharField(max_length=256)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )
    email = models.EmailField()
    level = models.CharField(max_length=16, choices=SponsorshipLevel.choices, default=SponsorshipLevel.partner)
    approved = models.BooleanField(default=False)

    def __str__(self):
        sponsoring = '[{}] {}'.format('Approved' if self.approved else 'Pending', self.name)
        if self.organization:
            return '{} | {}'.format(sponsoring, self.organization)
        return sponsoring


class PackageItem(ActiveModel):
    description = MarkdownxField()

    def __str__(self):
        return self.description[0:100]


class Package(ActiveModel):
    level = models.CharField(max_length=16, choices=SponsorshipLevel.choices)
    amount = MoneyField(max_digits=16, decimal_places=0, default_currency='EUR')
    description = MarkdownxField()
    items = models.ManyToManyField(PackageItem)

    def __str__(self):
        return '[{}] {}'.format(self.level, self.amount)

    @property
    def limit(self):
        if self.level == SponsorshipLevel.partner:
            return 'No Limits'
        return LIMITS[self.level]

    @property
    def is_over(self):
        count = Sponsor.objects.filter(level=self.level).count()
        if count >= LIMITS[self.level]:
            return True
        return False