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
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

    def __str__(self):
        return _("%(store)s %(weekday)s (%(from_hour)s - %(to_hour)s)") % {
            'store': self.store,
            'weekday': self.weekday,
            'from_hour': self.from_hour,
            'to_hour': self.to_hour
        }


class ClosingRules(models.Model):
    """
    Used to overrule the OpeningHours. This will "close" the store due to
    public holiday, annual closing or private party, etc.
    """
    class Meta:
        verbose_name = _('Closing Rule')
        verbose_name_plural = _('Closing Rules')
        ordering = ['start']

    store = models.ForeignKey(Owner)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    reason = models.TextField(_('Reason'), null=True, blank=True)

    def __str__(self):
        return _("%(store)s is closed from %(start)s to %(end)s\
        due to %(reason)s") % {
            'store': self.store.name,
            'start': str(self.start),
            'end': str(self.end),
            'reason': self.reason
        }
