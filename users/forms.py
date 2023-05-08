from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from users.models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')