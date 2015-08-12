from django.conf import settings
from django.db import models
from model_utils import Choices
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel
from profile.models import Lister, Address



class Listing(TimeStampedModel):
    STATUS = Choices(
        ('open', _('Open')),
        ('closed', _('Closed')),
        ('soon', _('Openning Soon')),
        ('shut_down', _('Shut Down'))
    )

    lister = models.ForeignKey(Lister, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS)
    address = models.ForeignKey(Address, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.status, self.title)
    class Meta:
        db_table = 'listing'
