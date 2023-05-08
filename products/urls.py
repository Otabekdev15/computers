from django.urls import path
from .views import ArticleListView, ArticleDetailView, AddReviewView, EditReviewView, DeleteReviewView, DeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article'),
    path('<int:id>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReviewView.as_view(), name='reviews'),
    path('<int:article_id>/reviews/<int:review_id>/edit/', EditReviewView.as_view(), name='edit-review'),
    path('<int:article_id>/reviews/<int:review_id>/delete/confirm', DeleteReviewView.as_view(), name='delete-review'),
    path('<int:article_id>/reviews/<int:review_id>/delete/', DeleteView.as_view(), name='delete')
]

