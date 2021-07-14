from django.urls import path
from . import views


urlpatterns = [
    path("article", views.ArticleListView.as_view(), name="article-list"),
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="article-detail"),
    path("generic/article", views.GenericApiListView.as_view(), name="generic-article"),
    path("generic/article/<int:pk>", views.GenericApiListView.as_view(), name="generic-article-list"),
]