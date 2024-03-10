# movies/models.py
from django.db import models
from django.contrib.auth.models import User
from typing import Union


class Genre(models.Model):
    id: Union[int, models.BigAutoField, None] = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Rating(models.Model):
    id: Union[int, models.BigAutoField, None] = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    rating_value =  models.DecimalField(max_digits=2, decimal_places=1, choices=[
        (1.0, '1.0'),
        (1.5, '1.5'),
        (2.0, '2.0'),
        (2.5, '2.5'),
        (3.0, '3.0'),
        (3.5, '3.5'),
        (4.0, '4.0'),
        (4.5, '4.5'),
        (5.0, '5.0'),
    ])

    def __str__(self):
        return f"{self.name} - {self.rating_value}"


class Cast(models.Model):
    id: Union[int, models.BigAutoField, None] = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    # Add other fields like bio, birth date, etc. as needed

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    id: Union[int, models.BigAutoField, None] = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    cast = models.ManyToManyField(Cast, through='Role', related_name='movies')

    def __str__(self):
        return f"{self.title}" # what to show when on the django admin


class Role(models.Model):
    ROLE_CHOICES = (
        ('actor', 'Actor'),
        ('director', 'Director'),
        ('producer', 'Producer'),
        ('writer', 'Writer'),
    )
    id: Union[int, models.BigAutoField, None] = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='roles')
    cast_member = models.ForeignKey(Cast, on_delete=models.CASCADE, related_name='roles')
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    top_billing = models.BooleanField(default=False)

    class Meta:
        unique_together = ('movie', 'cast_member')
        

    def __str__(self):
        return f"{self.movie.title} -- {self.cast_member.name} ({self.role})"
