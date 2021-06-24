from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk 20 mins",
    "march": "Learn Django",
    "april": "Eat no meat apr",
    "may": "Walk may",
    "june": "Learn June",
    "july": "Eat july",
    "august": "Walk august",
    "september": "Learn Sept",
    "october": "Eat october",
    "november": "Learn November",
    "december": "Dec walk",
}


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    my_month = months[month-1]
    redirect_url = reverse("monthly-challenge", args=[my_month])
    print("Redirect Url {}".format(redirect_url))
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        response = monthly_challenges[month]
        response_html = "<h1>{}</h1>".format(response)
    except:
        response_error = "<h1 style='color:red'>{}</h1>".format("Month Not Valid")
        return HttpResponseNotFound(response_error)
    return HttpResponse(response_html)

