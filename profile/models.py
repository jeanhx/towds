from django.conf import settings
from django.db import models
# from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Zipcode(models.Model): #gis_models.Model):
    code = models.CharField(max_length=5, null=True, blank=True)
    # poly = gis_models.PolygonField(null=True, blank=True)
    # objects = gis_models.GeoManager()


class Address(models.Model):# gis_models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.ForeignKey(Zipcode, null=True, blank=True)
    # objects = gis_models.GeoManager()


class Lister(TimeStampedModel):
    user = models.ForeignKey(User, null=True, blank=True, default=None)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, null=True, blank=True)
    home_address = models.ForeignKey(Address, null=True, blank=True)

    class Meta:
        db_table = 'lister'

    def __unicode__(self):
        return "%s -  %s" % (selfname, self.home_address.city)