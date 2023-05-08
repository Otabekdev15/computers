from django.urls import path

from users.views import CustomUserView, PersonalView, PersonEditView

urlpatterns = [
    path('register', CustomUserView.as_view(), name='register'),
    path('personal', PersonalView.as_view(), name='personal'),
    path('edit_info', PersonEditView.as_view(), name='edit')
]