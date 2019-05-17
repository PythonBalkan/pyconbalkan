from rest_framework import serializers

from pyconbalkan.sponsorship.models import Sponsorship


class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = '__all__'
