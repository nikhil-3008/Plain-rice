from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .models import Investment ,Investor

# Create your views here.


def Home(request):
    return render(request,'index.html')

def Profile(request):
    return render(request,'profile/profilepage.html')

def investorinfo(request):
    return render(request,'basicInfo.html')


def dashboard1(request):
    investments = Investment.objects.all()  
    data = {'investments': investments}
    return render(request, 'Dashboard1.html', data)

def dashboard2(request):
    investors = Investor.objects.all()  
    data = {'investors': investors}
    return render(request, 'Dashboard2.html', data)

    
def investnow(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prize = request.POST.get('prize')
        time = request.POST.get('time')
      

       

        temp = ((int(prize) * int(time) / 12 ) / 100) + int(prize)
        
        investment = Investment.objects.create(
            name=name,
            # user=request.user,
            prize=prize,
            time=time,
            total_amount=temp
        )
        investment.save
        return redirect('dashboard1')

    return render(request, 'profile/make_investment.html')

def investor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prize = request.POST.get('prize')
        
      
        investor = Investor.objects.create(
            name=name,
            # user=request.user,
            prize=prize,
            
        )
        investor.save()
        return redirect('dashboard2')

    return render(request, 'basicInfo.html')







