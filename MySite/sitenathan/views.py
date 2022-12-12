from django.shortcuts import render,redirect
from sitenathan import forms
# Create your views here.

from sitenathan.ai_funcs import tweet_prediction

def homepage(request):
    return render(request,'homepage.html')


def about_me(request):
    return render(request,'about_me.html')

def front(request):
    return render(request,"front.html")


def parcours(request):
    return render(request,"mon-parcours.html")


def tweet(request):
    if request.method=="GET":
        form  = forms.TweetForm()
        context = {"form":form,"bar_position":-25}
        return render(request,"tweet.html",context=context)

    if request.method=="POST":
        form  = forms.TweetForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("text")
            value_predicted = tweet_prediction(message)
            bar_position = int(50*value_predicted[0][0]-50)
            with open('/home/nathan/f.txt','a') as f:
                f.write(str(value_predicted[0][0]))
            context = {"bar_position":bar_position,"form":form}

        return render(request,'tweet.html',context=context)
        

def projets(request):
    return render(request,"projects_list.html")