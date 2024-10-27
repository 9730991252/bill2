from django import template
from user.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
register = template.Library()

@register.inclusion_tag('inclusion_tag/office/total_amount.html')
def total_amount():
    cash = User_cash.objects.all().aggregate(Sum('amount'))
    if cash:
        total_cash = cash['amount__sum']
        if total_cash != None:
            total_cash=float(math.floor(total_cash))
        else: 
            total_cash = 0
        p = Phonepe.objects.all().aggregate(Sum('amount'))
        phonepe = p['amount__sum']
        if phonepe != None:
            phonepe_amount=float(math.floor(phonepe))
        else:
            phonepe_amount = 0
        b = Bank_account.objects.all().aggregate(Sum('amount'))
        bank = b['amount__sum']
        if bank != None:
            bank_amount=float(math.floor(bank))
        else:
            bank_amount = 0
        total = (total_cash + phonepe_amount + bank_amount)
        return {
            'total_cash':total_cash,
            'phonepe_amount':phonepe_amount,
            'bank_amount':bank_amount,
            'total':total
        } 
    
@register.inclusion_tag('inclusion_tag/office/total_pending_amount.html')
def total_pending_amount():
    user = User.objects.all()
    total = 0
    if user:
        total = Bill.objects.all().aggregate(Sum('pending_amount'))
    return {
        'user':user,   
        'total':total['pending_amount__sum']
    } 
    
    
@register.inclusion_tag('inclusion_tag/office/total_cash_amount.html')
def total_cash_amount():
    cash = User_cash.objects.all()
    if cash:
        ca = cash.aggregate(Sum('amount'))
        total_cash = ca['amount__sum']
    return {
        'cash':cash,
    'total_cash':total_cash

    } 
    
@register.inclusion_tag('inclusion_tag/office/total_phonepe_amount.html')
def total_phonepe_amount():
    phone = Phonepe.objects.all()
    if phone:
        pa = phone.aggregate(Sum('amount'))
        total_phonepe = pa['amount__sum']
    return {
        'phone':phone,
    'total_phonepe':total_phonepe

    } 
    
@register.inclusion_tag('inclusion_tag/office/total_bank_amount.html')
def total_bank_amount():
    bank = Bank_account.objects.all()
    if bank:
        pa = bank.aggregate(Sum('amount'))
        total_bank = pa['amount__sum']
    return {
        'bank':bank,
        'total_bank':total_bank
    } 
    
@register.simple_tag()
def user_pending_bill_amount(user_id):
    if user_id:
        bill = Bill.objects.filter(user_id=user_id).aggregate(Sum('pending_amount'))
        if bill['pending_amount__sum'] == None:
            return 0
        else:
            return bill['pending_amount__sum']
    
    

@register.simple_tag()
def from_phonepe_transfer(id):
    if id:
        phonepe = Phonepe.objects.filter(id=id).first()
        return str(phonepe.mobile)[6:10]

@register.simple_tag()
def from_bank_transfer(id):
    if id:
        bank = Bank_account.objects.filter(id=id).first()
        return str(bank.number)[10:15]