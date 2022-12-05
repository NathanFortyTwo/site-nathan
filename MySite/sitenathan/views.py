from django.shortcuts import render

# Create your views here.



def homepage(request):
    return render(request,'homepage.html')


def about_me(request):
    return render(request,'about_me.html')

def front(request):
    return render(request,"front.html")