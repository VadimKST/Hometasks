from rest_framework import viewsets


from applications.twits.models import Movie, Review, Comment
from applications.twits.serializers import MovieSerializer, ReviewSerializer, CommentSerializer


class MovieViewSet(viewsets.ModelViewSet):
    model = Movie
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    model = Review
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()