from django.urls import path
from . import views

urlpatterns = [
    path("", views.reviews),
    path("thank-you", views.thank_you)
]
