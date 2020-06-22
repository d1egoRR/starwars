from django.db import models


class CharacterRating(models.Model):
    character_id = models.IntegerField()
    rating = models.IntegerField()

    @classmethod
    def rating_values(self, character_id):
        result = CharacterRating.objects.filter(
            character_id=character_id
        ).aggregate(
            max_rating=models.Max('rating'),
            avg_rating=models.Avg('rating')
        )

        avg_rating = result['avg_rating'] if result['avg_rating'] else 0
        return {
            'max_rating': result['max_rating'],
            'average_rating': round(avg_rating, 1)
        }

    def __str__(self):
        return f'Character {self.character_id}, Rating {self.rating}'
