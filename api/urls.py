from django.urls import path

from .apiviews import CharacterAPIView


urlpatterns = [
    path(
        'character/<int:character_id>/',
        CharacterAPIView.as_view(),
        name='character'
    ),
    path(
        'character/<int:character_id>/rating/',
        CharacterAPIView.as_view(),
        name='character-rating'
    ),
]
