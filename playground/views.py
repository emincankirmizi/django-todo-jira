from django.shortcuts import render


# Create your views here.


def room(request, room_name):
    return render(request, 'playground/playground.html', {
        'room_name': room_name
    })
