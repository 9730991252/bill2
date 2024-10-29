from django.shortcuts import redirect, render
from .models import *
from user.models import *
# Create your views here.
def office_home(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        user_cash = User_cash.objects.all()
        context={
            'e':e,
            'user_cash':user_cash
        }
        return render(request, 'office/office_home.html', context)
    else:
        return redirect('login')
     
def user(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if 'add_user'in request.POST:
            name = request.POST.get('name').upper()
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            user_type = request.POST.get('user_type')
            if User.objects.filter(mobile=mobile).exists() or User.objects.filter(user_type_id=user_type).exists():
                pass
            else:
                User(
                    name = name,
                    mobile = mobile,
                    pin = pin,
                    user_type_id = user_type,
                    ).save()
                return redirect('user')
        if 'edit_user'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name').upper()
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            user_type = request.POST.get('user_type')
            User(
                id = id,
                name = name,
                mobile = mobile,
                pin = pin,
                user_type_id = user_type,
            ).save()
            return redirect('user')
        if 'active'in request.POST:
            id = request.POST.get('id')
            u = User.objects.filter(id=id).first()
            u.status = 0
            u.save()
            return redirect('user')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            u = User.objects.filter(id=id).first()
            u.status = 1
            u.save()
            return redirect('user')
        context={
            'e':e,
            'user_type':User_type.objects.filter(status=1),
            'user':User.objects.all(),
        }
        return render(request, 'office/user.html', context)
    else:
        return redirect('login')
    

def type(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if 'add_type'in request.POST:
            name = request.POST.get('name').upper()
            if User_type.objects.filter(name=name).exists():
                pass
            else:
                User_type(
                    name = name
                    ).save()
                return redirect('type')
        if 'edit_type'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name').upper()
            User_type(
                id = id,
                name = name
                ).save()
            return redirect('type')
        if 'active'in request.POST:
            id = request.POST.get('id')
            u = User_type.objects.filter(id=id).first()
            u.status = 0
            u.save()
            return redirect('type')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            u = User_type.objects.filter(id=id).first()
            u.status = 1
            u.save()
            return redirect('type')
        context={
            'e':e,
            'user_type':User_type.objects.all()
        }
        return render(request, 'office/type.html', context)
    else:
        return redirect('login')

def phonepe(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if 'add_phonepe_number'in request.POST:
            user = request.POST.get('user')
            number = request.POST.get('number')
            if Phonepe.objects.filter(mobile=number).exists():
                pass
            else:
                Phonepe(
                    user_id = user,
                    mobile = number
                ).save() 
        if 'edit_phonepe_number'in request.POST:
            id = request.POST.get('id')
            user = request.POST.get('user')
            number = request.POST.get('number')
            Phonepe(
                id=id,
                user_id = user,
                mobile = number
            ).save() 
        if 'active'in request.POST:
            id = request.POST.get('id')
            u = Phonepe.objects.filter(id=id).first()
            u.status = 0
            u.save()
            return redirect('phonepe')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            u = Phonepe.objects.filter(id=id).first()
            u.status = 1
            u.save()
            return redirect('phonepe')
        context={
            'e':e,
            'user':User.objects.filter(status=1),
            'phonepe':Phonepe.objects.all()
        }
        return render(request, 'office/phonepe.html', context)
    else:
        return redirect('login')
    
def bank_account(request):
    if request.session.has_key('office_mobile'):
        office_mobile = request.session['office_mobile']
        e=Office_employee.objects.filter(mobile=office_mobile).first()
        if 'add_bank_account'in request.POST:
            user = request.POST.get('user')
            bank_name = request.POST.get('bank_name')
            number = request.POST.get('number')
            if Bank_account.objects.filter(number=number).exists():
                pass
            else:
                Bank_account(
                    user_id = user,
                    number = number,
                    bank_name = bank_name
                ).save() 
            return redirect('bank_account')
        if 'edit_bank_account'in request.POST:
            id = request.POST.get('id')
            user = request.POST.get('user')
            number = request.POST.get('number')
            bank_name = request.POST.get('bank_name')
            Bank_account(
                id=id,
                user_id = user,
                number = number,
                bank_name = bank_name
            ).save() 
            return redirect('bank_account')
        if 'active'in request.POST:
            id = request.POST.get('id')
            u = Bank_account.objects.filter(id=id).first()
            u.status = 0
            u.save()
            return redirect('bank_account')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            u = Bank_account.objects.filter(id=id).first()
            u.status = 1
            u.save()
            return redirect('bank_account')
        context={
            'e':e,
            'user':User.objects.filter(status=1),
            'bank_account':Bank_account.objects.all() 
        }
        return render(request, 'office/bank_account.html', context)
    else:
        return redirect('login')
    