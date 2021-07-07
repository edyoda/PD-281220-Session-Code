from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
class UserRegistrationView(CreateView):
    template_name = "feedbackusers/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('review-index')
