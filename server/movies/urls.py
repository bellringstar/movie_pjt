from django.urls import path
from . import views

urlpatterns = [
    path('movies/',views.movie_list), #전체 영화 목록
    path('movies/search/',views.movie_search), #검색창
    path('movies/<int:movie_pk>/', views.movie_detail), #상세 영화 정보
    path('<int:movie_pk>/movie_review/', views.movie_reviews), #특정 영화의 전체 리뷰 받아오기
    path('<int:user_pk>/user_review/', views.user_reviews), #특정 유저가 쓴 전체 리뷰 받아오기
    path('review/<int:review_pk>/', views.change_review), #특정 리뷰 수정,삭제
    path('<int:review_pk>/comment/', views.review_comment), #특정 리뷰에 달린 코멘트 받아오기
    path('<int:movie_pk>/reviews/', views.create_review), #특정 영화의 리뷰 생성
    path('movies/tag/', views.tags), #모든 태그 목록 가져오기
    path('<int:movie_pk>/tag/', views.add_tags), #영화에 태그 추가하기
    path('<int:user_pk>/', views.userinfo), #특정 유저 정보
    path('get_movie/', views.get_recent_movie), #최신영화 30개
    path('get_popularity_movie/', views.get_popularity_movie), #인기영화 30개
]