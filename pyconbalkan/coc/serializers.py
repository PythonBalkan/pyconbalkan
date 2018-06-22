from rest_framework import serializers
from .models import CodeOfConduct, ResponseGuide


class CodeOfConductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeOfConduct
        fields = '__all__'


class ResponseGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseGuide
        fields = '__all__'
