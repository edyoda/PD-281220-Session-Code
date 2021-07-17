from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView

from .forms import ProfileForm
from .models import UserProfile


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    

class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/upload_profile.html"
    success_url = "/profiles"
    fields = "__all__"


class ListProfiles(ListView):
    model = UserProfile
    template_name = "profiles/list_profiles.html"
    context_object_name = "profiles"


# Create your views here.
# class CreateProfileView(View):

#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/upload_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             user_profile = UserProfile(user_image = request.FILES.get('user_image'))
#             user_profile.save()
#             return HttpResponseRedirect("/profiles")
#         return render(request, "profiles/upload_profile.html", {
#             "form": submitted_form
#         })
