from rest_framework import serializers
from pyconbalkan.timetable.models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
