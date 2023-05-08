from rest_framework import serializers
from products.models import Articles
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'title', 'body', 'author', 'date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
