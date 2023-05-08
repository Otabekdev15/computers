from django.contrib import admin

from products.models import Articles, BookReview

# Register your models here.
admin.site.register(Articles)
admin.site.register(BookReview)

