from django.urls import path
from .views import *

urlpatterns = [
    path('rooms',RoomView.as_view())
]
