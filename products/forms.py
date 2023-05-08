from django import forms

from products.models import BookReview


class ArticleReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('comment',)
