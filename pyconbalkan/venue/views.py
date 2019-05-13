from django.shortcuts import render


def venue_view(request):
    return render(request, 'venue.html')
