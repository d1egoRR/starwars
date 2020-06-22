import json

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import CharacterRating


class CharacterAPIViewTestCase(APITestCase):

    def test_get(self):
        # context
        CharacterRating.objects.create(character_id=1, rating=3)
        CharacterRating.objects.create(character_id=1, rating=5)
        CharacterRating.objects.create(character_id=1, rating=4)
        CharacterRating.objects.create(character_id=1, rating=4)

        response = self.client.get('/api/character/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)
        self.assertEqual('Luke Skywalker', data['name'])
        self.assertEqual(4.0, data['average_rating'])
        self.assertEqual(5, data['max_rating'])

    def test_post_ok(self):
        params = {'rating': 2}
        response = self.client.post(
            '/api/character/1/rating/', params, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = json.loads(response.content)
        self.assertTrue(data['ok'])

    def test_post_rating_range_error(self):
        params = {'rating': 6}
        response = self.client.post(
            '/api/character/1/rating/', params, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = json.loads(response.content)
        self.assertFalse(data['ok'])

    def test_post_without_params(self):
        params = {}
        response = self.client.post(
            '/api/character/1/rating/', params, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = json.loads(response.content)
        self.assertFalse(data['ok'])
