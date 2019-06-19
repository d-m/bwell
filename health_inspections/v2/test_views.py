from django import urls
from rest_framework import status, test
from .. import models


class EstablishmentViewSetTest(test.APITestCase):
    fixtures = ['establishments.json', 'inspections.json']
    url = urls.reverse('v2:establishment-list')

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['count'],
            models.Establishment.objects.count()
        )
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_detail(self):
        response = self.client.get(self.url, args=[1, ])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, 'application/json')


class InspectionViewSetTest(test.APITestCase):
    fixtures = ['establishments.json', 'inspections.json']
    url = urls.reverse('v2:inspection-list')

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['count'],
            models.Inspection.objects.count()
        )
        self.assertEqual(response.accepted_media_type, 'application/json')

    def test_detail(self):
        response = self.client.get(self.url, args=[1, ])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, 'application/json')
