from django.conf import settings
from django.db import models
from django.contrib.gis.db import models as gis_models
from model_utils import Choices
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel


class Listing(TimeStampedModel):
    STATUS = Choices(
        ('open', _('Open')),
        ('closed', _('Closed')),
        ('soon', _('Openning Soon')),
        ('shut_down', _('Shut Down'))
    )

    lister = models.ForeignKey('profile.models.Lister')
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS)
    address = models.ForeignKey('Address')
    lon = models.FloatField()
    lat = models.FloatField()

    def __unicode__(self):
        return "%s - %s" % (self.status, self.title)
    class Meta:
        db_table = 'listing'


class Zipcode(gis_models.Model):
    code = models.CharField(max_length=5)
    poly = gis_models.PolygonField()
    objects = gis_models.GeoManager()


class Address(gis_models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.ForeignKey(Zipcode)
    objects = gis_models.GeoManager()
