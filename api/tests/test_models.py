import unittest

from api.models import CharacterRating


class CharacterRatingTestCase(unittest.TestCase):

    def test_rating_values(self):
        # context
        CharacterRating.objects.create(character_id=1, rating=3)
        CharacterRating.objects.create(character_id=1, rating=4)
        CharacterRating.objects.create(character_id=1, rating=2)
        CharacterRating.objects.create(character_id=1, rating=3)

        result = CharacterRating.rating_values(character_id=1)

        self.assertIn('average_rating', result)
        self.assertIn('max_rating', result)
        self.assertEqual(4, result['max_rating'])
        self.assertEqual(3.0, result['average_rating'])

        CharacterRating.objects.create(character_id=1, rating=5)
        result = CharacterRating.rating_values(character_id=1)

        self.assertEqual(5, result['max_rating'])
        self.assertEqual(3.4, result['average_rating'])
