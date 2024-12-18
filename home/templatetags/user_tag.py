from django import template
from user.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
register = template.Library()


@register.simple_tag()
def phonepe_transfer_user(from_phonepe_id):
    from_phonepe = Phonepe.objects.filter(id=from_phonepe_id).first()
    return f'From = {from_phonepe.user.user_type.name} - {from_phonepe.user.name}  {from_phonepe.mobile}'



@register.simple_tag()
def check_verify_pending_phone_and_bank(bill_id):
    status = 0
    if bill_id:
        if Phonepe_transition.objects.filter(bill_id=bill_id, self_verify_status=0).exists():
            status = 1
        if Bank_transition.objects.filter(bill_id=bill_id, self_verify_status=0).exists():
            status = 1
    return status

@register.simple_tag()
def calculate_dayes(main_date):
    if main_date:
        d = date.today() - main_date
    return d.days

@register.inclusion_tag('inclusion_tag/office/bill_received_detail.html')
def bill_received_detail(id):
    if id:
        phonepe = Phonepe_transition.objects.filter(bill_id=id)
        bank = Bank_transition.objects.filter(bill_id=id)
        cash = Cash_amount.objects.filter(bill_id=id)
    return{
        'phonepe':phonepe,
        'bank':bank,
        'cash':cash,
    }
    
@register.inclusion_tag('inclusion_tag/office/bill_received_detail.html')
def pement_verify_pending(id):
    if id:
        phonepe = Phonepe_transition.objects.filter(bill_id=id,self_verify_status=0)
        bank = Bank_transition.objects.filter(bill_id=id,self_verify_status=0)
        cash = []
    return{
        'phonepe':phonepe,
        'bank':bank,
        'cash':cash,
    }


    