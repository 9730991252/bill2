from django.shortcuts import redirect, render
from office.models import * 
from user.models import * 
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.session.has_key('office_mobile'):
        return redirect('office_home')
    if request.session.has_key('user_mobile'):
        return redirect('user_home')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            e= Office_employee.objects.filter(mobile=number,pin=pin,status=1)
            if e:
                request.session['office_mobile'] = request.POST["number"]
                return redirect('office_home')
            u = User.objects.filter(mobile=number,pin=pin,status=1)
            if u:
                request.session['user_mobile'] = request.POST["number"]
                return redirect('user_home')
    return render(request, 'home/login.html')

    
    
def office_logout(request):
    if request.session.has_key('office_mobile'):
        del request.session['office_mobile']
    return redirect('/')
        
def user_logout(request):
    if request.session.has_key('user_mobile'):
        del request.session['user_mobile']
    return redirect('/')