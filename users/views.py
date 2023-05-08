from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from users.forms import CustomUserForm, CustomUserChangeForm


# Create your views here.
class CustomUserView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class PersonalView(View):
    def get(self, request):
        return render(request, 'registration/personal.html')


class PersonEditView(View, LoginRequiredMixin):
    def get(self, request):
        edit_form = CustomUserChangeForm(instance=request.user)
        return render(request, 'registration/edit_info.html', {'edit_form': edit_form})

    def post(self, request):
        edit_form = CustomUserChangeForm(instance=request.user, data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('personal')

        return render(request, 'registration/edit_info.html', {'edit_form': edit_form})
