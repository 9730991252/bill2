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

def bill_in_verify_phonepe(request):
    if request.method == 'GET':
        phonepe_transition_id = request.GET['phonepe_transition_id']
        phonepe_transition = Phonepe_transition.objects.filter(id=phonepe_transition_id).first()
        if phonepe_transition.self_verify_status == 0:
           phonepe_transition.self_verify_status = 1
           phonepe_transition.save()
    return JsonResponse({'status': 1})

def transfer_verify_phonepe(request):
    if request.method == 'GET':
        phonepe_transfer_id = request.GET['phonepe_transfer_id']
        phonepe_transfer = Phonepe_transfer.objects.filter(id=phonepe_transfer_id).first()
        if phonepe_transfer.to_verify_status == 0:
            phonepe_transfer.to_verify_status = 1
            phonepe_transfer.save()
    return JsonResponse({'status': 1})

def bill_in_verify_bank(request):
    if request.method == 'GET':
        bank_transition_id = request.GET['bank_transition_id']
        bank_transition = Bank_transition.objects.filter(id=bank_transition_id).first()
        if bank_transition.self_verify_status == 0:
            bank_transition.self_verify_status = 1
            bank_transition.save()
    return JsonResponse({'status': 1})

def transfer_verify_cash_to_bank(request):
    if request.method == 'GET':
        cash_transfer_to_bank_id = request.GET['cash_transfer_to_bank_id']
        cash_transfer_to_bank = Cash_transfer_to_bank.objects.filter(id=cash_transfer_to_bank_id).first()
        if cash_transfer_to_bank.to_verify_status == 0:
            cash_transfer_to_bank.to_verify_status = 1
            cash_transfer_to_bank.save()
    return JsonResponse({'status': 1})

def transfer_verify_bank(request):
    if request.method == 'GET':
        bank_transfer_id = request.GET['bank_transfer_id']
        bank_transfer = Bank_transfer.objects.filter(id=bank_transfer_id).first()
        if bank_transfer.to_verify_status == 0:
            bank_transfer.to_verify_status = 1
            bank_transfer.save()
    return JsonResponse({'status': 1})

def edit_bill_name(request):
    if request.method == 'GET':
        id = request.GET['id']
        edit_bill_name_input = request.GET['edit_bill_name_input']
        bill= Bill.objects.filter(id=id).first()
        bill.bill_number = edit_bill_name_input
        bill.save()
    return JsonResponse({'edit_bill_name_input': edit_bill_name_input})