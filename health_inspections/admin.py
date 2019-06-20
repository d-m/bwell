# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Establishment, Inspection


admin.site.register(Establishment)
admin.site.register(Inspection)
