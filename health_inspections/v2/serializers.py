from rest_framework import serializers
from ..models import Establishment, Inspection


class EstablishmentSerializer(serializers.HyperlinkedModelSerializer):
    inspections = serializers.HyperlinkedRelatedField(
        view_name='v2:inspection-detail',
        read_only=True,
        many=True
    )
    url = serializers.HyperlinkedIdentityField(view_name='v2:establishment-detail')

    class Meta:
        model = Establishment
        fields = (
            'id',
            'url',
            'name',
            'dba_name',
            'aka_name',
            'license_number',
            'risk_level',
            'address',
            'city',
            'state',
            'zip_code',
            'inspections',
        )


class InspectionSerializer(serializers.HyperlinkedModelSerializer):
    establishment = serializers.HyperlinkedRelatedField(
        view_name='v2:establishment-detail',
        read_only=True
    )
    url = serializers.HyperlinkedIdentityField(view_name='v2:inspection-detail')

    class Meta:
        model = Inspection
        fields = (
            'id',
            'url',
            'inspection_id',
            'inspection_type',
            'inspection_results',
            'violations',
            'establishment',
        )
