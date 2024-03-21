from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
        "january":"eat no meat",
        "febuary":"walk daily",
        "march" :"go to the gym",
        "april" :"eat no meat",
        "may" : "walk daily",
        "june" :"go to the gym",
        "july" : "eat no meat",
        "auguest" :"walk daily",
        "september":"go to the gym",
        "october" : "eat no meat",
        "november" : "walk daily",
        "december" : None
  }

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request,"challenges/index.html",{
         "months":months
    })

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    
    if month >len(months):
        return HttpResponseNotFound("This month is not found")

    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge" , args =[redirect_month]) #/challenges/january
    return  HttpResponseRedirect(redirect_path)
    
def monthly_challenge(request,month):

    try :
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404()
    
    