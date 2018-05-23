from rest_framework import serializers

from pyconbalkan.cfp.models import Cfp


class CfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cfp
        fields = '__all__'
