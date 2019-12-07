from django.shortcuts import render
from tracking.models import Sighting
import json
import numpy as np


def list_sightings(request):

    context = {'object_list': Sighting.objects.values_list('pk', flat=True).order_by('pk')}

    return render(request, 'tracking/list_sightings.html', context)


def add_sighting(request):

    data = json.loads(request.body.decode('utf-8'))

    s = Sighting()
    s.Latitude = data.get('Latitude')
    s.Longitude = data.get('Longitude')
    s.Unique_Squirrel_ID = data.get('Unique Squirrel ID')
    s.Shift = data.get('Shift')
    s.Date = data.get('Date')
    s.Age = data.get('Age')
    s.Primary_Fur_Color = data.get('Primary Fur Color')
    s.Location = data.get('Location')
    s.Specific_Location = data.get('Specific Location')
    s.Running = data.get('Running')
    s.Chasing = data.get('Chasing')
    s.Climbing = data.get('Climbing')
    s.Eating = data.get('Eating')
    s.Foraging = data.get('Foraging')
    s.Other_Activities = data.get('Other Activities')
    s.Kuks = data.get('Kuks')
    s.Quaas = data.get('Quaas')
    s.Moans = data.get('Moans')
    s.Tail_flags = data.get('Tail flags')
    s.Tail_twitches = data.get('Tail twitches')
    s.Approaches = data.get('Approaches')
    s.Indifferent = data.get('Indifferent')
    s.Runs_from = data.get('Runs from')

    s.save()


def update_or_delete(request, pk):
    # update
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        s = Sighting.objects.get(pk=pk)

        s.Latitude = data.get('Lattitude') or s.Latitude
        s.Longitude = data.get('Longitude') or s.Longitude
        s.Unique_Squirrel_ID = data.get('Unique Squirrel ID') or s.Unique_Squirrel_ID
        s.Shift = data.get('Shift') or s.Shift
        s.Date = data.get('Date') or s.Date
        s.Age = data.get('Age') or s.Age
        s.Primary_Fur_Color = data.get('Primary Fur Color') or s.Primary_Fur_Color
        s.Location = data.get('Location') or s.Location
        s.Specific_Location = data.get('Specific Location') or s.Specific_Location
        s.Running = data.get('Running') or s.Running
        s.Chasing = data.get('Chasing') or s.Chasing
        s.Climbing = data.get('Climbing') or s.Climbing
        s.Eating = data.get('Eating') or s.Eating
        s.Foraging = data.get('Foraging') or s.Foraging
        s.Other_Activities = data.get('Other Activities') or s.Other_Activities
        s.Kuks = data.get('Kuks') or s.Kuks
        s.Quaas = data.get('Quaas') or s.Quaas
        s.Moans = data.get('Moans') or s.Moans
        s.Tail_flags = data.get('Tail flags') or s.Tail_flags
        s.Tail_twitches = data.get('Tail twitches') or s.Tail_twitches
        s.Approaches = data.get('Approaches') or s.Approaches
        s.Indifferent = data.get('Indifferent') or s.Indifferent
        s.Runs_from = data.get('Runs from') or s.Runs_from

        s.save()
    # delete
    elif request.method == "DELETE":
        Sighting.objects.get(pk=pk).delete()
