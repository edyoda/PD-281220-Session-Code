from django.urls import path
from .views import CreateProfileView, ListProfiles


urlpatterns = [
    path("", CreateProfileView.as_view()),
    path("list", ListProfiles.as_view()),
]
