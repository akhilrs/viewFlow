from django.db import models
from viewflow.models import Process, Task


class Carrier(models.Model):
    DEFAULT = 'Default'

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def is_default(self):
        return self.name == Carrier.DEFAULT

    def __str__(self):
        return self.name


class Insurance(models.Model):
    company_name = models.CharField(max_length=50)
    cost = models.FloatField()

    def __str__(self):
        return f'{self.company_name} ${self.cost}'


class Shipment(models.Model):
    shipment_no = models.CharField(max_length=50)
    carrier = models.ForeignKey(Carrier, null=True)

    # Customer
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    # Shipment address
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)

    # Shipment data
    need_insurance = models.BooleanField(default=False)
    insurance = models.ForeignKey(Insurance, null=True)

    carrier_quote = models.IntegerField(default=0)
    