from django.contrib import admin
from .models import Artist, Genre, Artwork, Style, Period, savedArtworks
# Register your models here.
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Artwork)
admin.site.register(Style)
admin.site.register(Period)
admin.site.register(savedArtworks)

