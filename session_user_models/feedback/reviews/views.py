from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



from .forms import ReviewForm
from .models import Review


# Create your views here.
class IndexView(TemplateView):
    template_name = "reviews/r_index.html"
    

class ReviewsView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "reviews/reviews.html"
    success_url = "/thank-you"
    model = Review
    form_class = ReviewForm


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["message"] = "This is a message !!"
        return context_data


class AllReviews(ListView): # Getting Data
    template_name = "reviews/all_reviews.html"
    model = Review 
    context_object_name = "reviews"


class SpecificReview(DetailView):
    template_name = "reviews/specific_review.html"
    model = Review
    context_object_name = "review" 
