from rest_framework import serializers

from applications.twits.models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ()


class ReviewSerializer(serializers.ModelSerializer):
    comment = CommentSerializer

    class Meta:
        model = Review
        exclude = ()


class MovieSerializer(serializers.ModelSerializer):
    reveiw = ReviewSerializer

    class Meta:
        model = Movie
        exclude = ()




