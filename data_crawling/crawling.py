import requests
import json
import openai
from time import sleep

auth = "tmdb"
# url = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page=1" #전체 리스트
# url = f"https://api.themoviedb.org/3/movie/{movie_id}&language=ko-KR" #디테일
# url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-Kr' #배우,스탭(이미지 포함)


def get_embedding(text):
    openai.api_key = "openai"
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input = text
    )
    
    return response["data"][0]["embedding"]
    


def get_movies(page):
    url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={page}"
    headers = {
    "accept": "application/json",
    "Authorization": auth
    }
    response = requests.get(url, headers=headers)
    movie_list = response.json()
    return movie_list

def get_detail(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=ko-KR"
    headers = {
        "accept": "application/json",
        "Authorization": auth
    }
    response = requests.get(url, headers=headers)
    movie_detail = response.json()
    return movie_detail

def get_actors(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"
    headers = {
        "accept": "application/json",
        "Authorization": auth
    }
    response = requests.get(url, headers=headers)
    movie_credit = response.json()
    actors = []
    cnt = 0
    for cast in movie_credit['cast']:
        if(cnt == 3):
            break
        actors.append({
            'id':cast['id'],
            'name':cast['name'],
            'profile_path':cast['profile_path'],
            'character':cast['character']
        })
        cnt += 1

    return actors

def get_director(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=ko-KR"
    headers = {
        "accept": "application/json",
        "Authorization": auth
    }
    response = requests.get(url, headers=headers)
    movie_credit = response.json()
    director = []
    
    for cast in movie_credit['crew']:
        if cast['job'] == 'Director':
            director.append({
                'id':cast['id'],
                'name':cast['name'],
                'profile_path':cast['profile_path']
            })
    return director






cnt = 0

def create_data(page):
    global cnt
    movie_list = get_movies(page=page)

    for movie in movie_list['results']:
        # print(movie)
        movie_id = movie['id']
        movie_detail = get_detail(movie_id)
        actors = get_actors(movie_id)
        actor_list = []
        for actor in actors:
            actor_list.append(actor['id'])
        director = get_director(movie_id)
        #django에서는 arrayField 사용해 리스트 저장
        #model에 정의한 칼럼 추출
        overview_embeddings = get_embedding(movie['overview'])
        title_embedding = get_embedding(movie['title'])

        data.append({
            'model': 'movies.movie',
            'fields':{
                'movie_id': movie_id,
                'title': movie['title'],
                'overview' : movie['overview'],
                'release_date' : movie_detail['release_date'],
                'poster_path' : movie['poster_path'] ,
                'backdrop_path': movie['backdrop_path'],
                'genres': movie['genre_ids'],
                'actors': actor_list,
                'director': [director[0]['id']] if director else [],
                'adult': movie_detail['adult'],
                'runtime':movie_detail['runtime'],
                'popularity':movie['popularity'],
                'overview_embedding': f'{overview_embeddings}',
                'title_embedding':f'{title_embedding}'
            }
        })
        
        for actor in actors:
            if(actor['id'] not in actor_key):
                actor_key.append(actor['id'])
                actor_data.append({
                    'model': 'movies.actor',
                    'fields':{
                        'actor_id': actor['id'],
                        'name': actor['name'],
                        'profile_path': actor['profile_path']
                    }
                })
        if director:
            if(director[0]['id'] not in director_key):
                director_key.append(director[0]['id'])
                director_data.append({
                    'model':'movies.director',
                    'fields':{
                    'director_id' : director[0]['id'],
                    'name': director[0]['name'],
                    'profile_path': director[0]['profile_path']
                    }
                })
        for genre in movie_detail['genres']:
            if(genre['id'] not in genre_key):
                genre_key.append(genre['id'])
                genres_data.append({
                    'model':'movies.genre',
                    'fields':{
                        'genre_id': genre['id'],
                        'name': genre['name']
                    }
                })
        
    

    print(cnt)
    cnt += 1



genre_key = []
actor_key = []
director_key = []
data = []
actor_data = []
genres_data = []
director_data = []

for i in range(1, 35):
    create_data(i)
    sleep(25)


with open('movies.json', 'a', encoding='UTF-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
with open('actors.json', 'a', encoding='UTF-8') as outfile:
    json.dump(actor_data, outfile, ensure_ascii=False)
with open('genres.json', 'a', encoding='UTF-8') as outfile:
    json.dump(genres_data, outfile, ensure_ascii=False)
with open('director.json', 'a', encoding='UTF-8') as outfile:
    json.dump(director_data, outfile, ensure_ascii=False)
