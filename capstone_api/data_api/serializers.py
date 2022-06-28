from rest_framework import serializers 
from .models import VacationEvent 

class VacationEventSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = VacationEvent  # tell django which model to use
        fields = ('id', 'name', 'date','description', 'image', 'location', 'price', 'notes',) # tell django which fields to include
