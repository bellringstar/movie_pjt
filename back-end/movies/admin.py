from django.contrib import admin
from .models import Review,Tag,TagMovieUser,Movie,Comment,Actor,Genre,Director
# Register your models here.

admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(TagMovieUser)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Director)
