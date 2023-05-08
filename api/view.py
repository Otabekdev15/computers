from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from products.models import Articles
from .serializers import ArticleSerializer, UserSerializer
from products.permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
