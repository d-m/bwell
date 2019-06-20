from rest_framework import serializers
from ..models import Establishment, Inspection


class EstablishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Establishment
        fields = (
            'id',
            'name',
            'dba_name',
            'aka_name',
            'license_number',
            'risk_level',
            'address',
            'city',
            'state',
            'zip_code',
        )


class InspectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inspection
        fields = (
            'id',
            'inspection_id',
            'inspection_type',
            'inspection_results',
            'violations',
            'establishment',
        )