from django.db import models

from authentication.models import MyUser


class Order(models.Model):
    user = models.ForeignKey(
        to=MyUser,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()
    amount = models.FloatField()
    confirmation_code = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
