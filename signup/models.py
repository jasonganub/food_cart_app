from django.db import models
from django.contrib.auth.models import User


# The fields (first_name, last_name, username, email) will be
# accesed via the built in User model.

class Seeker(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
