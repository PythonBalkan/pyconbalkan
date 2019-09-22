
from django.shortcuts import render

from pyconbalkan.timetable.models import Room, Slot
from django.db.models.functions import TruncDate


def timetable_view(request):
    rooms = Room.objects.all()
    slots = Slot.objects.all()
    dates = slots.annotate(date=TruncDate('from_date')).values('date').distinct()
    slots_by_date = {}

    for i, date in enumerate(dates):
        slots_by_date[i] = Slot.objects.filter(from_date__date=date['date'])

    context = {
        'slots_by_date': slots_by_date,
        'rooms': rooms,
        'dates': dates
    }
    return render(request, 'timetable.html', context)
