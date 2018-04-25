from rest_framework import serializers

from pyconbalkan.conference.models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'
