from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from products.forms import ArticleReviewForm
from products.models import Articles, BookReview


# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'products/article.html'


class ArticleDetailView(View):
    def get(self, request, id):
        article = Articles.objects.get(id=id)
        review_form = ArticleReviewForm()

        return render(request, 'products/detail.html', {'article': article, 'review_form': review_form})


class AddReviewView(View, LoginRequiredMixin):
    def post(self, request, id):
        article = Articles.objects.get(id=id)
        review_form = ArticleReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                article=article,
                user=request.user,
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse('detail', kwargs={'id': article.id}))

        return render(request, 'products/detail.html', {'article': article, "review_form": review_form})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, article_id, review_id):
        article = Articles.objects.get(id=article_id)
        review = article.comments.get(id=review_id)
        review_form = ArticleReviewForm(instance=review)

        return render(request, 'products/edit_review.html', {'article': article,
                                                             'review': review,
                                                             'review_form': review_form})

    def post(self, request, article_id, review_id):
        article = Articles.objects.get(id=article_id)
        review = article.comments.get(id=review_id)
        review_form = ArticleReviewForm(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('detail', kwargs={'id': article.id}))

        return render(request, 'products/edit_review.html', {'article': article,
                                                             'review': review,
                                                             'review_form': review_form})


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, article_id, review_id):
        article = Articles.objects.get(id=article_id)
        review = article.comments.get(id=review_id)
        return render(request, 'products/delete_review.html', {'article': article, 'review': review})


class DeleteView(LoginRequiredMixin, View):
    def get(self, request, article_id, review_id):
        article = Articles.objects.get(id=article_id)
        review = article.comments.get(id=review_id)

        review.delete()
        return redirect(reverse('detail', kwargs={'id': article.id}))




