from django.urls import path
from . import views

urlpatterns = [
    path('api/events', views.VacationEventList.as_view(), name='VacationEvent_list'), # api/VacationEvent will be routed to the VacationEventList view for handling
    path('api/events/<int:pk>', views.VacationEventDetail.as_view(), name='VacationEvent_detail'), # api/VacationEvent will be routed to the EventDetail view for handling
]
