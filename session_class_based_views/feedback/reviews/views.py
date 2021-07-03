from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


from .forms import ReviewForm
from .models import Review


# Create your views here.
# class ReviewsView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/reviews.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, "reviews/reviews.html", {
#             "form": form
#         })


# class ReviewsView(FormView):
#     template_name = "reviews/reviews.html"
#     form_class = ReviewForm
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewsView(CreateView):
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


# class AllReviews(TemplateView):
#     template_name = "reviews/all_reviews.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class AllReviews(ListView): # Getting Data
    template_name = "reviews/all_reviews.html"
    model = Review 
    context_object_name = "reviews"


# class SpecificReview(TemplateView):
#     template_name = "reviews/specific_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         request_id = kwargs["id"]
#         review = Review.objects.get(pk=request_id)
#         context["review"] = review
#         return context

class SpecificReview(DetailView): # Get some data
    template_name = "reviews/specific_review.html"
    model = Review
    context_object_name = "review" # Name of of your model in all small letters
