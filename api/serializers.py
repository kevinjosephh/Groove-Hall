from dataclasses import fields
from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'code', 'host', 'guestPause', 'skipVotes', 'created']