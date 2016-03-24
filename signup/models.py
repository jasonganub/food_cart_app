from django.db import models
from django.contrib.auth.models import User


# The fields (first_name, last_name, username, email) will be
# accesed via the built in User model.
class Seeker(models.Model):
    user = models.OneToOneField(User)
    user.first_name = models.CharField(max_length=30)
    user.last_name = models.CharField(max_length=30)
    user.username = models.CharField(max_length=150)
    user.email = models.EmailField(max_length=100)
    user.password = models.CharField(max_length=100)

    @classmethod
    def create(cls, firstname, lastname, username, email, password):
        new_seeker = cls(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password)
        return new_seeker

    def __str__(self):
        return self.user.username
