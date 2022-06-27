from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import EventSerializer
from .models import Event

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = EventSerializer # tell django what serializer to use

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer