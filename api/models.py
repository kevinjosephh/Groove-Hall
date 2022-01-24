from django.db import models
import string
import random
# Create your models here.

def generateRoomCode():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


class Room(models.Model):
    host = models.CharField(max_length=20,unique=True)
    code = models.CharField(max_length=4,unique=True)
    guestPause = models.BooleanField(null=False,default=False)
    skipVotes = models.IntegerField(null=False,default=1)
    created = models.DateTimeField(auto_now_add=True)