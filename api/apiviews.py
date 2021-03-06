
import json

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CharacterRating
from .services.star_wars import StarWarsService


@cache_page(60*60*2)
@api_view(['GET'])
def character_info(request, character_id):
    """
    Se muestra los datos del personaje
    """
    character = StarWarsService.get_character_info(character_id)
    rating_values = CharacterRating.rating_values(character_id)
    character['average_rating'] = rating_values['average_rating']
    character['max_rating'] = rating_values['max_rating']
    return Response(character)


@api_view(['POST'])
def character_rating(request, character_id):
    """
    Se agrega puntaje al personaje
    """
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        return Response(
            {'ok': False, 'error': 'Debe enviar el parametro'},
            status.HTTP_400_BAD_REQUEST
        )

    rating = data.get('rating', None)
    if rating is None:
        return Response(
            {'ok': False, 'error': 'Debe enviar el Rating'},
            status.HTTP_400_BAD_REQUEST
        )

    if rating not in range(1, 6):
        return Response(
            {'ok': False, 'error': 'Rating debe estar entre 1 y 5'},
            status.HTTP_400_BAD_REQUEST
        )

    character_rating = CharacterRating.objects.create(
        character_id=character_id,
        rating=rating
    )

    return Response({'ok': True}, status.HTTP_201_CREATED)
