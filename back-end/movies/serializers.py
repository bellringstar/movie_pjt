from rest_framework import serializers
from .models import Genre,Actor,Director,Movie,Tag,Review,Comment,TagMovieUser
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ('user',)
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie_id', 'is_liked',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagMovieUser
        fields = '__all__'
        read_only_fields=('user', 'movie_id',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'self_introduction', 'profile_image')
        read_only_fields = ('username',)