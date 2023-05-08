from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import CustomUser


# Create your models here.
class Articles(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


