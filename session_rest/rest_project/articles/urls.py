from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("article", views.ArticleViewSet, basename="viewset-article")
router.register("generic", views.ArticleGenericViewSet, basename="viewset-generic")


urlpatterns = [
    path("viewset/", include(router.urls)),
    path("article", views.ArticleListView.as_view(), name="article-list"),
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="article-detail"),
]