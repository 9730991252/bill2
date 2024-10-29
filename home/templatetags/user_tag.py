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