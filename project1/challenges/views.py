from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 30 minutes every day",
    "march": "Learn Django for atleast 20 minutes every day",
    "april": "Don't watch TV for the entire month",
    "may": "Spend only 40 minutes a day on mobile for the entire month",
    "june": "Complete reading 'Lord of the Rings'",
    "july": "Only watch 1 movie in july",
    "august": "No Pizza in august",
    "september": "Only talk in English",
    "october": "Learn about the usage of Adobe Photoshop",
    "november": "Pass the driving test",
    "december": None

}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month <= 0:
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/"+redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()