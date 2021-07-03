from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewsView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.AllReviews.as_view()),
    path("reviews/<int:pk>", views.SpecificReview.as_view()), # slug
]
