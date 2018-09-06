from django.shortcuts import render


def info_view(request):
    return render(request, 'info.html')
