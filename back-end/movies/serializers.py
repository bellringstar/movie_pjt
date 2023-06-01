from rest_framework import serializers
from .models import Genre,Actor,Director,Movie,Tag,Review,Comment,TagMovieUser
from django.contrib.auth import get_user_model
User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'overview_kr', 'release_date', 'poster_path', 'runtime', 'popularity')

class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'is_liked')

class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    movie_title = serializers.CharField(source='movie_id.title', read_only=True)
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
        read_only_fields = ('user', 'review_id',)

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