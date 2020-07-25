from django.urls import path

from .apiviews import character_info, character_rating


urlpatterns = [
    path('character/<int:character_id>/', character_info, name='character'),
    path(
        'character/<int:character_id>/rating/',
        character_rating,
        name='character-rating'
    ),
]
