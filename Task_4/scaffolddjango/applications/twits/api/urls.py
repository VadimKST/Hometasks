from django.urls import path
from rest_framework import routers

from applications.twits.api.movie import MovieViewSet, ReviewViewSet, CommentViewSet

movie_router = routers.DefaultRouter()
movie_router.register(r'movie', MovieViewSet, basename='application.twits')
movie_router.register(r'review', ReviewViewSet, basename='application.twits')
movie_router.register(r'comment', CommentViewSet, basename='application.twits')
urlpatterns = movie_router.urls
