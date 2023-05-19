from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True)


class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True)

class Movie(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    overview = models.TextField(blank=True)
    release_date = models.TextField(blank=True)
    poster_path = models.TextField(null=True)
    backdrop_path = models.TextField(null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    director = models.ManyToManyField(Director, blank=True)
    adult = models.BooleanField()
    runtime = models.IntegerField(blank=True)
    popularity = models.IntegerField(blank=True)
    overview_embedding = models.TextField(blank=True)
    title_embedding = models.TextField(blank=True)


class Tag(models.Model):
    title = models.CharField(max_length=100)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like')


class Comment(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    content = models.TextField() 


class TagMovieUser(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
