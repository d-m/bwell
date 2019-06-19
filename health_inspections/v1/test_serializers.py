from rest_framework import test
import serializers
from .. import models

ESTABLISHMENT_EXPECTED_KEYS = {
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
}

INSPECTION_INSPECTED_KEYS = {
    'id',
    'inspection_id',
    'inspection_type',
    'inspection_results',
    'violations',
    'establishment',
}


class EstablishmentSerializerTest(test.APITestCase):
    fixtures = ['establishments.json', 'inspections.json']

    def setUp(self):
        self.factory = test.APIRequestFactory()
        self.establishment = models.Establishment.objects.first()

    def test_serialization(self):
        """Make sure that the expected serializer keys are present"""
        serialized_establishment = serializers.EstablishmentSerializer(
            self.establishment
        )
        self.assertSetEqual(
            set(serialized_establishment.fields.keys()),
            ESTABLISHMENT_EXPECTED_KEYS
        )


class InspectionSerializerTest(test.APITestCase):
    fixtures = ['establishments.json', 'inspections.json']

    def setUp(self):
        self.factory = test.APIRequestFactory()
        self.inspection = models.Inspection.objects.first()

    def test_serialization_keys(self):
        """Make sure that the expected serializer keys are present"""
        serialized_inspection = serializers.InspectionSerializer(
            self.inspection
        )
        self.assertSetEqual(
            set(serialized_inspection.fields.keys()),
            INSPECTION_INSPECTED_KEYS
        )
