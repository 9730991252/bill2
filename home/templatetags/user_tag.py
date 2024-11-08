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


    