from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# The fields (first_name, last_name, username, email) will be
# accesed via the built in User model.
class Seeker(AbstractBaseUser):
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name',
        'email', 'password']

    def __str__(self):
        return self.user_name
