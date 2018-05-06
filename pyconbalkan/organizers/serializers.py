from rest_framework import serializers

from pyconbalkan.conference.models import Conference
from pyconbalkan.organizers.models import Volunteer


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
