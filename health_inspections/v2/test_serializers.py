from django import urls
from rest_framework import test
import serializers
from .. import models

ESTABLISHMENT_EXPECTED_KEYS = {
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
}

INSPECTION_INSPECTED_KEYS = {
    'id',
    'url',
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

    def test_url_field(self):
        """Make sure that the V2 API points to V2 urls"""
        url = urls.reverse(
            'v2:establishment-detail',
            args=[self.establishment.id]
        )
        request = self.factory.get(url)
        serialized_establishment = serializers.EstablishmentSerializer(
            self.establishment,
            context={'request': request}
        )
        self.assertEqual(
            request.build_absolute_uri(),
            serialized_establishment.data['url']
        )

    def test_inspections_field(self):
        """Make sure that V2 API points to V2 urls"""
        url = urls.reverse(
            'v2:establishment-detail',
            args=[self.establishment.id]
        )
        request = self.factory.get(url)
        serialized_establishment = serializers.EstablishmentSerializer(
            self.establishment,
            context={'request': request}
        )
        inspections = self.establishment.inspections.all()
        inspections_urls = [
            urls.reverse('v2:inspection-detail', args=[inspection.id])
            for inspection in inspections
        ]
        expected_data = [
            self.factory.get(inspection_url).build_absolute_uri()
            for inspection_url in inspections_urls
        ]
        self.assertListEqual(
            serialized_establishment.data['inspections'],
            expected_data
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

    def test_inspections_field(self):
        """Make sure that V2 API points to V2 urls"""
        url = urls.reverse(
            'v2:inspection-detail',
            args=[self.inspection.id]
        )
        request = self.factory.get(url)
        serialized_inspection = serializers.InspectionSerializer(
            self.inspection,
            context={'request': request}
        )
        establishment = self.inspection.establishment
        establishment_url = urls.reverse(
            'v2:establishment-detail',
            args=[establishment.id]
        )
        expected = self.factory.get(establishment_url).build_absolute_uri()
        self.assertEqual(
            serialized_inspection.data['establishment'],
            expected
        )
