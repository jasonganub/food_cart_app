from django.db import models
from django.utils.translation import gettext as _


WEEKDAYS = [
  (1, _("Monday")),
  (2, _("Tuesday")),
  (3, _("Wednesday")),
  (4, _("Thursday")),
  (5, _("Friday")),
  (6, _("Saturday")),
  (7, _("Sunday")),
]


class Owner(models.Model):
    name = models.CharField(max_length=100)
    ethnic = models.CharField(max_length=100)

    # TODO: add menu and location
    # name, hours, culture/ethnic type

    def __str__(self):
        return self.name


class OpeningHours(models.Model):
    store = models.ForeignKey(Owner)
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
