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

