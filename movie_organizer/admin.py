# movies/admin.py
from django.contrib import admin
from .models import Movie, Genre, Cast, Role
from .models import Rating

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Cast)
admin.site.register(Role)