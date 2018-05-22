from rest_framework import serializers
from pyconbalkan.sponsors.models import Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'
