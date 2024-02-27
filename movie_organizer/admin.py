# movies/admin.py
from django.contrib import admin
from .models import Movie, Genre, Cast, Role

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Role)