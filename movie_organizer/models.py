# movies/models.py
from django.db import models
from django.contrib.auth.models import User
from typing import Union


class Genre(models.Model):
    id: Union[int, models.BigAutoField, None] = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


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
        return f"{self.title}"


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
