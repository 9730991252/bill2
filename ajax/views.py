from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import *
from user.models import *
# Create your views here.

def out_user_cash (request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        cash= User_cash.objects.filter(user_id=user_id).first()
        context={
            'cash':cash.amount,
            'user_id':user_id
        }
        t = render_to_string('ajax/user/out_user_cash.html',context)
    return JsonResponse({'t': t})
        
def out_user_phonepe (request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        phonepe= Phonepe.objects.filter(user_id=user_id)

        context={
            'phonepe':phonepe,
            'user_id':user_id
        }
        t = render_to_string('ajax/user/out_user_phonepe.html',context)
    return JsonResponse({'t': t})
        
def out_bank(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        bank= Bank_account.objects.filter(user_id=user_id)

        context={
            'bank':bank,
            'user_id':user_id
        }
        t = render_to_string('ajax/user/out_bank.html',context)
    return JsonResponse({'t': t})

def transfer_user_cash(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        cash= User_cash.objects.filter(user_id=user_id).first()
        context={
            'cash':cash,
            'user_id':user_id,
            'cash_users':User_cash.objects.filter(user__status=1)
        }
        t = render_to_string('ajax/user/transfer_user_cash.html',context)
    return JsonResponse({'t': t})

def transfer_user_cash_to_bank(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        cash= User_cash.objects.filter(user_id=user_id).first()
        context={
            'cash':cash,
            'user_id':user_id,
            'to_bank':Bank_account.objects.filter(status=1)
        }
        t = render_to_string('ajax/user/transfer_user_cash_to_bank.html',context)
    return JsonResponse({'t': t})
        
def transfer_user_phonepe(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        phonepe= Phonepe.objects.filter(user_id=user_id)

        context={
            'phonepe':phonepe,
            'user_id':user_id,
            'all_phonepe':Phonepe.objects.filter(status=1).exclude(user_id=user_id)
        }
        t = render_to_string('ajax/user/transfer_user_phonepe.html',context)
    return JsonResponse({'t': t})

def transfer_user_bank(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        bank= Bank_account.objects.filter(user_id=user_id)

        context={
            'bank':bank,
            'user_id':user_id,
            'to_bank':Bank_account.objects.filter(status=1).exclude(user_id=user_id)
        }
        t = render_to_string('ajax/user/transfer_user_bank.html',context)
    return JsonResponse({'t': t})

def search_bill(request):
    if request.method == 'GET':
        bill_input = request.GET['bill_input']
        if bill_input:
            bill= Bill.objects.filter(bill_number__icontains=bill_input)
        if bill_input == '':
            bill= ''
        context={
            'bill':bill[0:10],
        }
        t = render_to_string('ajax/user/search_bill.html',context)
    return JsonResponse({'t': t})