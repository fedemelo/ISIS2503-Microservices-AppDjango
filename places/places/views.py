from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place = Place()
        place.name = data_json["name"]
        place.save()
        return HttpResponse("successfully created place")
    
def PlaceDelete(request, id):
    if request.method == 'DELETE':
        place = Place.objects.get(id=id)
        place.delete()
        return HttpResponse("successfully deleted place")
    
def PlacesDelete(request):
    if request.method == 'DELETE':
        Place.objects.all().delete()
        return HttpResponse("successfully deleted places")