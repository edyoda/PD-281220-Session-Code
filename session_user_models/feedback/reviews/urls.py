from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="review-index"),
    path("add", views.ReviewsView.as_view(), name="review-add"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews", views.AllReviews.as_view(), name="all-reviews"),
    path("reviews/<int:pk>", views.SpecificReview.as_view(), name="selected-review"),
]
