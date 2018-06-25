from rest_framework import serializers
from pyconbalkan.sponsoring.models import Sponsoring


class SponsoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsoring
        fields = '__all__'
