from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def reviews(request):
    print("Method : {} ".format(request.method))
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("UserName : {}, Password : {}".format(username, password))
        if username == "" or password == "":
            return render(request, "reviews/reviews.html", {
                "has_error": True
            })
        return HttpResponseRedirect("/thank-you")
    return render(request, "reviews/reviews.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")