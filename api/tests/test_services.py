import unittest

from api.services.star_wars import StarWarsService


class StarWarsServiceTestCase(unittest.TestCase):

    def test_get_specie_name(self):
        endpoints = list()
        result = StarWarsService.get_specie_name(endpoints)
        self.assertIsNone(result)

        endpoints.append('https://swapi.dev/api/species/1/')
        result = StarWarsService.get_specie_name(endpoints)
        self.assertEqual('Human', result)

    def test_get_homeworld_info(self):
        endpoint = 'https://swapi.dev/api/planets/1/'
        result = StarWarsService.get_homeworld_info(endpoint)
        self.assertEqual('Tatooine', result['name'])
        self.assertEqual('200000', result['population'])
        self.assertGreaterEqual(10, result['know_residents_count'])

    def test_get_character_info(self):
        result = StarWarsService.get_character_info(character_id=1)
        self.assertEqual('Luke Skywalker', result['name'])
        self.assertEqual('172', result['height'])
        self.assertEqual('77', result['mass'])
        self.assertIn('population', result['homeworld'])
