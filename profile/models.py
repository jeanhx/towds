from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Lister(TimeStampedModel):
    user = models.ForeignKey(User, null=True, blank=True, default=None)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, null=True, blank=True)
    home_address = models.ForeignKey('ads.models.Address', null=True, blank=True)

    class Meta:
        db_table = 'lister'

    def __unicode__(self):
        return "%s -  %s" % (selfname, self.home_address.city)

