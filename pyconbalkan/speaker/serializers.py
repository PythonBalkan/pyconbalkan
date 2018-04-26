from rest_framework import serializers

from pyconbalkan.speaker.models import Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'
