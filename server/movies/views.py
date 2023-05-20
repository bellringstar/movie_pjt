from datetime import datetime
from . import embedding
import torch
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer, MovieListSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer,TagListSerializer, TagSerializer
from .models import Genre,Actor,Director,Movie,Tag,Review,Comment,TagMovieUser
# Create your views here.


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_recent_movie(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    data_list = serializer.data
    sorted_data = sorted(data_list, key=lambda x: datetime.strptime(x['release_date'], '%Y-%m-%d') if x['release_date'] else datetime(2999, 12, 31), reverse=True)
    return Response(sorted_data[:30])

@api_view(['GET'])
def get_popularity_movie(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    data_list = serializer.data
    sorted_data = sorted(data_list, key=lambda x: x['popularity'], reverse=True)
    return Response(sorted_data[:30])


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_tag(request, movie_pk):
    pass

@api_view(['GET'])
def movie_reviews(reqeust, movie_pk):
    reviews = get_list_or_404(Review, movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_reviews(request, user_pk):
    reviews = get_list_or_404(Review, user=user_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

# @permission_classes([IsAuthenticated])
@api_view(['PUT', 'DELETE'])
def change_review(request,review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def review_comment(request, review_pk):
    comment = get_list_or_404(Comment, review_id = review_pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)

# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, movie_id = movie_pk)
    user = get_object_or_404(get_user_model(), id=request.user.id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie, user = user) #유저 에러
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def tags(request):
    tags = get_list_or_404(Tag)
    serializer = TagListSerializer(tags, many=True)
    return Response(serializer.data)

# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_tags(request, movie_pk):
    #request에 tag_id를 받아온다
    if request.method == 'POST':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        user = get_object_or_404(get_user_model(), id=request.user.id)
        tag = get_object_or_404(Tag, id=request.data['tag_id'])
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT'])
def userinfo(request, user_pk):
    user = get_object_or_404(get_user_model(), id=user_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    # 자기소개, 이미지 수정
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def movie_search(request):
    movies = get_list_or_404(Movie)
    serializer = serializer = MovieListSerializer(movies, many=True)
    #request에는 사용자가 입력한 문장
    query = request.data['query']
    genres = embedding.find_genre(query)
    genres_list= embedding.to_list(genres)
    genre_dic = {'adventure' : 12,'fantasy':14,'animation':16, 'drama':18,
                 'horror': 27, 'action':28, 'comedy':35, 'history':36, 'western':37,
                 'thriller':53, 'crime':80, 'documentary':99, 'sf':878, 'mystery':9648,
                 'music':10402, 'romance':10749, 'family':10751, 'war':10752, 'tv movie':10770}
    print(genres_list)
    if genres_list:
        genres_list = [genre_dic[genre.lower().strip()] for genre in genres_list]
        print(genres_list)
        embeddings = embedding.get_embedding(genres)
        vector_a = torch.tensor(embeddings)
        similarity = []
        for data in serializer.data:
            if len(set(data['genres'])&set(genres_list)):
                vector_b = torch.tensor(eval(data['overview_embedding']))
                similarity_score = embedding.cosine_similarity(vector_a, vector_b)
                # similarity.append({data['movie_id']:similarity_score})
                similarity.append({data['title']:similarity_score})
        sorted_data = sorted(similarity, key=lambda x: list(x.values())[0], reverse=True)
        
        return Response(sorted_data)
    else:
        return Response([{'err':"다시 시도해 주세요 내용이 짧다면 좀 더 길게 써주세요"}])
