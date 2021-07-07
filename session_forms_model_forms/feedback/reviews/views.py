from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.
# class ReviewView(View):
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

# class ReviewView(FormView): # GET # POST
#     template_name = "reviews/reviews.html"
#     form_class = ReviewForm
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    template_name = "reviews/reviews.html"
    success_url = "/thank-you"
    model = Review
    fields = "__all___"
    form_class = ReviewForm


# Get a single review based on an ID
# display all the reviews
class AllReviews(ListView):
    template_name = "reviews/all_reviews.html"
    model = Review # context_name = object_list
    context_object_name = "reviews"

    def get_queryset(self) -> QuerySet[T]:
        return super().get_queryset()


# class SingleReviewView(TemplateView):
#     template_name = "reviews/specific_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         review = Review.objects.get(pk=review_id)
#         context["review"] = review
#         return context

class SingleReviewView(DetailView): # Either fetch from PK or Slug
    template_name = "reviews/specific_review.html"
    model = Review # context_name = <Name of model>.lowerCase()
    context_object_name = "review"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works !!"
        return context