from rest_framework import serializers
from pyconbalkan.sponsors.models import Sponsor, Sponsoring


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class SponsoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsoring
        fields = '__all__'