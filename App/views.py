from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .models import Investment

# Create your views here.


def Home(request):
    return render(request,'index.html')

def Portfolio(request):
    investments = Investment.objects.filter(user = request.user)
    data = {
        'investments':investments
    }
    return render(request,'profile/portfolio.html',data)



def investnow(request):
    if request.method == 'POST':
        name = request.POST['name']
        prize = request.POST['prize']
        time = request.POST['time']
        risk = request.POST['risk']

        if(risk == 1):
            per = 8
        elif(risk == 2):
            per = 10
        else:
            per = 12

        temp = ((int(prize)*int(time)/12*per)/100) + int(prize)
        
        investment = Investment(name=name,user = request.user, prize=prize, time=time, risk=risk,total_amount=temp)

        investment.save()

        return redirect('portfolio')
        
    return render(request, 'profile/make_investment.html')

def addfunds(request):
    return render(request,'other/payment.html')

def about(request):
    return render(request,'about.html')





