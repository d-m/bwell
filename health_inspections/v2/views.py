# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from ..models import Establishment, Inspection
from .serializers import (
    EstablishmentSerializer,
    InspectionSerializer
)


class Establishment(viewsets.ReadOnlyModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class Inspection(viewsets.ReadOnlyModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
