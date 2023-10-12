from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .models import Investment

# Create your views here.


def Home(request):
    return render(request,'index.html')

def dashboard1(request):
    investments = Investment.objects.all()  # Use filter to get a queryset
    data = {'investments': investments}
    return render(request, 'Dashboard1.html', data)
    

def Portfolio(request):
    investments = Investment.objects.filter(user = request.user)
    data = {
        'investments':investments
    }
    return render(request,'Dashboard1.html',data)



def investnow(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prize = request.POST.get('prize')
        time = request.POST.get('time')
      

       

        temp = ((int(prize) * int(time) / 12 ) / 100) + int(prize)
        
        # Assuming you have an Investment model with the specified fields
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


def addfunds(request):
    return render(request,'other/payment.html')

def about(request):
    return render(request,'about.html')





