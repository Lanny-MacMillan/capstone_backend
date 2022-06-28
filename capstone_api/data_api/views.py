from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import VacationEventSerializer
from .models import VacationEvent

class VacationEventList(generics.ListCreateAPIView):
    queryset = VacationEvent.objects.all().order_by('id') 
    serializer_class = VacationEventSerializer # tell django what serializer to use

class VacationEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VacationEvent.objects.all().order_by('id')
    serializer_class = VacationEventSerializer