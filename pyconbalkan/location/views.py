from django.shortcuts import render


def venue_view(request):
    context = {}
    return render(request, 'venue.html', context)


def city_view(request):
    context = {}
    return render(request, 'city.html', context)


def guide_view(request):
    context = {"url": "https://www.youtube.com/embed/FLKXSgXNl8w"}
    return render(request, 'guide.html', context)


def accomodation_view(request):
    context = {}
    return render(request, 'accomodation.html', context)
