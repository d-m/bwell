# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from localflavor.us.models import USStateField, USZipCodeField


class Establishment(models.Model):
    dba_name = models.CharField(max_length=100)
    aka_name = models.CharField(max_length=100)
    license_number = models.IntegerField()
    risk_level = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = USZipCodeField()

    @property
    def name(self):
        if self.aka_name:
            return self.aka_name
        else:
            return self.dba_name


class Inspection(models.Model):
    inspection_id = models.IntegerField()
    inspection_date = models.DateField()
    inspection_type = models.CharField(max_length=50)
    inspection_results = models.CharField(max_length=50)
    violations = models.CharField(max_length=100)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
