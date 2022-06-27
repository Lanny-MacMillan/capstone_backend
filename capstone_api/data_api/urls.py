from django.urls import path
from . import views

urlpatterns = [
    path('api/events', views.EventList.as_view(), name='Event_list'), # api/Events will be routed to the EventList view for handling
    path('api/events/<int:pk>', views.EventDetail.as_view(), name='Event_detail'), # api/Events will be routed to the EventDetail view for handling
]
