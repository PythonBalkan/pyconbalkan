
from django.shortcuts import render

from pyconbalkan.timetable.models import Room, Slot
from django.db.models.functions import TruncDate

def timetable_sessionize_view(request):
    return render(request, 'timetable_sessionize.html')

def timetable_view(request):
    rooms = Room.objects.all()
    slots = Slot.objects.all()
    unique_dates = slots.annotate(date=TruncDate('from_date')).values('date').distinct()
    slots_by_date = {}
    dates = []

    for i, date in enumerate(unique_dates):
        slots_by_date[i] = Slot.objects.filter(from_date__date=date['date'])
        dates.append(date['date'])

    context = {
        'slots_by_date': slots_by_date,
        'rooms': rooms,
        'dates': sorted(dates)
    }
    return render(request, 'timetable.html', context)
