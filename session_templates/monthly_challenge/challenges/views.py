from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk for 20 mins everyday",
    "march": "Learn Django for 2hrs everyday",
    "april": "Learn Java and its application",
    "may": "Go skydiving",
    "june": "Go for a ladakh trip",
    "july": "Go deep water diving",
    "august": "Learn Flutter everday for 1 hr",
    "september": "Start running",
    "october": "Play football and learn a new skill every 2 day",
    "november": "Complete any book",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month Number")
    my_month = months[month-1]
    redirect_url = reverse("monthly-challenge", args=[my_month])
    print("Redirect Url {}".format(redirect_url))
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
        "challenge_text": text,
        "month" : month
    })
    

