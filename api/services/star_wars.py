import json
import requests


class StarWarsService:

    @classmethod
    def get_character_info(cls, character_id):
        endpoint = f'https://swapi.dev/api/people/{character_id}/'
        response = requests.get(endpoint)
        people = json.loads(response.content)
        return {
            'name': people['name'],
            'height': people['height'],
            'mass': people['mass'],
            'hair_color': people['hair_color'],
            'skin_color': people['skin_color'],
            'eye_color': people['eye_color'],
            'birth_year': people['birth_year'],
            'gender': people['gender'],
            'homeworld': cls.get_homeworld_info(people['homeworld']),
            'species_name': cls.get_specie_name(people['species']),
        }

    @classmethod
    def get_homeworld_info(cls, endpoint):
        response = requests.get(endpoint)
        planets = json.loads(response.content)
        return {
            'name': planets['name'],
            'population': planets['population'],
            'know_residents_count': len(planets['residents'])
        }

    @classmethod
    def get_specie_name(cls, species):
        if len(species) == 0:
            return None
        response = requests.get(species[0])
        specie = json.loads(response.content)
        return specie['name']
