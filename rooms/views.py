from django.shortcuts import render
from django.http import HttpResponse


def see_all_rooms(request):
    return HttpResponse("Hello!")


def see_one_room(request, pk):
    return HttpResponse(f"See one room with id:{pk}")
