import random

from datetime import datetime
from . import embedding
import torch
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Authentication Decorators

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from .serializers import MovieLikeSerializer,MovieSerializer,UserSerializer, MovieListSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer,TagListSerializer, TagSerializer
from .models import Genre,Actor,Director,Movie,Tag,Review,Comment,TagMovieUser
# Create your views here.


@api_view(['GET'])
def movie_list(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    movies_data = []
    for movie in serializer.data:
        data = {
            'movie_id': movie['movie_id'],
            'title': movie['title'],
            'poster_path': movie['poster_path'],
            'release_date': movie['release_date']
        }
        movies_data.append(data)
    return Response(movies_data)

@api_view(['GET'])
def get_recent_movie(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    movies_data = []
    for movie in serializer.data:
        data = {
            'movie_id': movie['movie_id'],
            'title': movie['title'],
            'poster_path': movie['poster_path'],
            'release_date': movie['release_date']
        }
        movies_data.append(data)
    sorted_data = sorted(movies_data, key=lambda x: datetime.strptime(x['release_date'], '%Y-%m-%d') if x['release_date'] else datetime(2999, 12, 31), reverse=True)
    return Response(sorted_data[:30])


@api_view(['GET'])
def get_popularity_movie(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    movies_data = []
    for movie in serializer.data:
        data = {
            'movie_id': movie['movie_id'],
            'title': movie['title'],
            'poster_path': movie['poster_path'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity']
        }
        movies_data.append(data)
    sorted_data = sorted(movies_data, key=lambda x: x['popularity'], reverse=True)
    return Response(sorted_data[:30])

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def movie_detail(request, movie_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def movie_reviews(reqeust, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_reviews(request, user_pk):
    reviews = Review.objects.filter(user_id=user_pk)

    print(reviews)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def like_review(request,review_pk):
    user_id = request.data['user_id']
    # user = get_object_or_404(get_user_model(),pk=user_id)
    user = get_user_model().objects.get(pk=user_id)
    # review = get_object_or_404(Review, pk=review_pk)
    review = Review.objects.get(pk=review_pk)
    if review.is_liked.filter(pk=user_id).exists():
        review.is_liked.remove(user)
    else:
        review.is_liked.add(user)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST','GET'])
def like_movie(request, user_pk):
    if(request.method == 'GET'):
        movies = Movie.objects.filter(is_liked = user_pk)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif(request.method == 'POST'):
        movie_id = request.data['movie_id']
        # user = get_object_or_404(get_user_model(), pk=user_pk)
        user = get_user_model().objects.get(pk=user_pk)
        # movie = get_object_or_404(Movie, movie_id=movie_id)
        movie = Movie.objects.get(movie_id=movie_id)
        serializer = MovieLikeSerializer(movie)
        if movie.is_liked.filter(pk=user_pk).exists():
            movie.is_liked.remove(user)
        else:
            movie.is_liked.add(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@permission_classes([IsAuthenticated])
@api_view(['PUT', 'DELETE'])
def change_review(request,review_pk):
    # review = get_object_or_404(Review, pk=review_pk)
    review = Review.objects.get(pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated])
@api_view(['GET','POST','DELETE','PUT'])
def review_comment(request, review_pk):
    if request.method == 'GET':
        # comment = get_list_or_404(Comment, review_id = review_pk)
        comment = Comment.objects.filter(review_id = review_pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # user = get_object_or_404(get_user_model(), id=request.data['userid'])
        user = get_user_model().objects.get(id=request.data['userid'])
        # review = get_object_or_404(Review, pk=review_pk)
        review = Review.objects.get(pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, review_id=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        # comment = get_object_or_404(Comment, pk=request.data['commentid'], user=request.data['userid'])
        comment = Comment.objects.get(pk=request.data['commentid'], user=request.data['userid'])
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        # comment = get_object_or_404(Comment, pk=request.data['commentid'], user=request.data['userid'])
        comment = Comment.objects.get(pk=request.data['commentid'], user=request.data['userid'])
        
        comment.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@permission_classes([IsAuthenticated])
@api_view(['POST','PUT','DELETE'])
def create_review(request, movie_pk):
    if request.method == 'POST':
        # movie = get_object_or_404(Movie, movie_id = movie_pk)
        movie = Movie.objects.get(movie_id = movie_pk)
        # user = get_object_or_404(get_user_model(), id=request.data['userid'])
        user = get_user_model().objects.get(id=request.data['userid'])
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=movie, user = user) #유저 에러
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        # review = get_object_or_404(Review, pk=request.data['id'])
        review = Review.objects.get(pk=request.data['id'])
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        # review = get_object_or_404(Review, pk=request.data['id'])
        review = Review.objects.get(pk=request.data['id'])
        review.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    
@api_view(['GET'])
def tags(request):
    # tags = get_list_or_404(Tag)
    tags = Tag.objects.all()
    serializer = TagListSerializer(tags, many=True)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['GET','POST', 'DELETE'])
def add_tags(request, movie_pk):
    if request.method == 'GET':
        tags = TagMovieUser.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        # movie = get_object_or_404(Movie, movie_id=movie_pk)
        movie = Movie.objects.get(movie_id=movie_pk)
        # user = get_object_or_404(get_user_model(),username=request.data['username'])
        user = get_user_model().objects.get(username=request.data['username'])
        # tag = get_object_or_404(Tag, id=request.data['tag_id'])
        tag = Tag.objects.get(id=request.data['tag_id'])        
        serializer = TagSerializer(data=request.data)            
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_id=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        movie = Movie.objects.get(movie_id=movie_pk)
        user = get_user_model().objects.get(username=request.data['username']) 
        tag = Tag.objects.get(id=request.data['tag_id'])        
        addtag = TagMovieUser.objects.get(movie_id_id=movie.movie_id,
                                tag_id_id=tag.id,
                                user_id=user.pk)
        
        addtag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT'])
def userinfo(request, username):
    if username.isdigit():
        # user = get_object_or_404(get_user_model(), id=username)
        user = get_user_model().objects.get(id=username)
    else:
        # user = get_object_or_404(get_user_model(), username=username)
        user = get_user_model().objects.get(username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    # 자기소개, 이미지 수정
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def movie_search(request):
    # movies = get_list_or_404(Movie)
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    #request에는 사용자가 입력한 문장
    query = request.data['query']
    genres = embedding.find_genre(query)
    genres_list= embedding.to_list(genres)
    genre_dic = {'adventure' : 12,'fantasy':14,'animation':16, 'drama':18,
                 'horror': 27, 'action':28, 'comedy':35, 'history':36, 'western':37,
                 'thriller':53, 'crime':80, 'documentary':99, 'sf':878, 'mystery':9648,
                 'music':10402, 'romance':10749, 'family':10751, 'war':10752, 'tv movie':10770}
    print(genres_list)
    vector_input = torch.tensor(embedding.get_embedding(query))
    
    if genres_list:
        genres_list = [genre_dic[genre.lower().strip()] for genre in genres_list]
        print(genres_list)
        embeddings = embedding.get_embedding(genres)
        vector_a = torch.tensor(embeddings)
        similarity = []
        for data in serializer.data:
            if len(set(data['genres'])&set(genres_list)):
                vector_overview = torch.tensor(eval(data['overview_embedding']))
                vector_title = torch.tensor(eval(data['title_embedding']))
                overview_similarity_score = embedding.cosine_similarity(vector_a, vector_overview)
                title_similarity_score = embedding.cosine_similarity(vector_input, vector_title)
                # similarity.append({data['movie_id']:similarity_score})
                similarity_score = 0.5*title_similarity_score + overview_similarity_score
                similarity.append({data['title']:similarity_score, 'popularity':data['popularity'], 'movie_id':data['movie_id'] })
        
        data = sorted(similarity, key=lambda x: x[next(iter(x))], reverse=True)[:30]
        sorted_data = sorted(data, key=lambda x: x['popularity'], reverse=True)[:15]
        random_selection = random.sample(sorted_data,5)
        return Response(random_selection)
    else:
        return Response({'err':"다시 시도해 주세요 내용이 짧다면 좀 더 길게 써주세요"})
