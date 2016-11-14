from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=100)
    ethnic = models.CharField(max_length=100)

    # TODO: add menu and location
    # name, hours, culture/ethnic type

    def __str__(self):
        return self.name
