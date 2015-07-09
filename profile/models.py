from django.db import models

from django.conf import settings

from django_extensions.db.models import TimeStampedModel
from towds.ads.model import Address

class Lister(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address', max_length=255)
    home_address = models.ForeignKey(Address)

    class Meta:
        db_table = 'lister'

    def __unicode__(self):
        return "%s -  %s" % (selfname, self.home_address.city)

