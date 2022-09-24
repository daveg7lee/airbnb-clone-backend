from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()

    return render(request, "all_rooms.html", {"rooms": rooms, "title": "Hello!"})


def see_one_room(request, pk):
    return HttpResponse(f"See one room with id:{pk}")
