from rest_framework import routers

from pyconbalkan.timetable.views import TimetableViewSet

router = routers.DefaultRouter()
router.register(r'timetable', TimetableViewSet)
