from django.db import models

from django.conf import settings

from django_extensions.db.models import TimeStampedModel
from towds.ads.model import Address

class Lister(TimeStampedModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255)
    home_address = models.ForiegnKey(Address)

    class Meta:
        db_table = 'lister'

    def __unicode__(self):
        return "%s -  %s" % (selfname, self.home_address.city)

    @property
    def pay_cycle(self):
        return PayCycle.factory(self.pay_cycle_json)

    def save(self, *args, **kwargs):
        if not self.borrower.jobs:
            self.status = 'primary'

        #if net_pay or salary not entered, set as entered amount
        self.net_pay = self.salary if not self.net_pay else self.net_pay
        self.salary = self.net_pay if not self.salary else self.salary
        super(Job, self).save(*args, **kwargs)
