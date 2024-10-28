from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages 

def user_home(request):
    if request.session.has_key('user_mobile'):
        user_mobile = request.session['user_mobile']
        user=User.objects.filter(mobile=user_mobile).first()
        c = Cash_amount.objects.filter(bill__user_id=user.id)
        amount = 0
        for c in c:
            amount += c.amount
        print(amount)   
        
        context={
            'user':user,
        }
        return render(request, 'user/user_home.html', context)
    else:
        return redirect('login')
    
def bill(request):
    if request.session.has_key('user_mobile'):
        user_mobile = request.session['user_mobile']
        user=User.objects.filter(mobile=user_mobile).first()
        if 'Add_bill'in request.POST:
            user_id = user.id
            user_type_id = user.user_type.id
            amount = request.POST.get('amount')
            pending_amount = amount
            bill_number = request.POST.get('bill_number')
            Bill(
                user_id=user_id,
                user_type_id=user_type_id,
                amount=amount,
                bill_number=bill_number,
                pending_amount=pending_amount
            ).save()
            return redirect('bill')
        context={
            'user':user,
            'bill':Bill.objects.filter(pending_amount_status=1, user_id=user.id),
            'all_bill':Bill.objects.filter(pending_amount_status=0, user_id=user.id).order_by('-id')
        }
        return render(request, 'user/bill.html', context)
    else:
        return redirect('login')
    
def bill_in(request, id):
    if request.session.has_key('user_mobile'):
        user_mobile = request.session['user_mobile']
        user=User.objects.filter(mobile=user_mobile).first()
        if 'Cash_add'in request.POST:
            bill = Bill.objects.filter(id=id).first()
            amount = request.POST.get('amount')
            if float(amount) <= bill.pending_amount:
                Cash_amount(
                    bill_id=id,
                    payment_type = 1,
                    amount = amount,
                    user_id=user.id
                ).save()
                bill.pending_amount -= float(amount)
                bill.save()
                return redirect(f'/user/bill_in/{id}')
            else:
                messages.warning(request,"पेंडिंग अमाऊंट पेक्षा कॅश अमाऊंट जास्त आहे . ")
        if 'phonepe_add'in request.POST:
            bill = Bill.objects.filter(id=id).first()
            amount = request.POST.get('amount')
            user = request.POST.get('user')
            if float(amount) <= bill.pending_amount:
                Phonepe_transition(
                    bill_id=id,
                    payment_type = 1,
                    amount = amount,
                    phonepe_id= user
                ).save()
                bill.pending_amount -= float(amount)
                bill.save()
                return redirect(f'/user/bill_in/{id}')
            else:
                messages.warning(request,"पेंडिंग अमाऊंट पेक्षा कॅश अमाऊंट जास्त आहे . ")
        if 'Bank_add'in request.POST:
            bill = Bill.objects.filter(id=id).first()
            amount = request.POST.get('amount')
            user = request.POST.get('user')
            if float(amount) <= bill.pending_amount:
                Bank_transition(
                    bill_id=id,
                    payment_type = 1,
                    amount = amount,
                    bank_id= user
                ).save()
                bill.pending_amount -= float(amount)
                bill.save()
                return redirect(f'/user/bill_in/{id}')
            else:
                messages.warning(request,"पेंडिंग अमाऊंट पेक्षा कॅश अमाऊंट जास्त आहे . ")
        if 'Complete_bill'in request.POST:
            b=Bill.objects.filter(id=id).first()
            b.pending_amount_status=0
            b.save()
            return redirect('/user/bill/') 
        context={
            'user':user,
            'bill':Bill.objects.filter(id=id).first(),
            'phonepe':Phonepe.objects.filter(status=1,user_id=user.id),
            'bank_account':Bank_account.objects.filter(status=1,user_id=user.id),
            'cash_amount':Cash_amount.objects.filter(bill_id=id),
            'phonepe_transition':Phonepe_transition.objects.filter(bill_id=id),
            'bank_transition':Bank_transition.objects.filter(bill_id=id),
        }
        return render(request, 'user/bill_in.html', context)
    else:
        return redirect('login')
    
def out(request):
    if request.session.has_key('user_mobile'):
        user_mobile = request.session['user_mobile']
        user=User.objects.filter(mobile=user_mobile).first()
        cash= User_cash.objects.filter(user_id=user.id).first()
        phonepe= Phonepe.objects.filter(user_id=user.id)
        bank= Bank_account.objects.filter(user_id=user.id)
        if 'User_out_cash' in request.POST:
            bill_name = request.POST.get('bill_name')
            user_id = request.POST.get('user_id')
            amount = request.POST.get('amount')
            Out_transition(
                user_id=user_id,
                out_bill_name=bill_name,
                amount=amount
            ).save()
            return redirect('/user/out/')
        if 'User_out_phonepe' in request.POST:
            bill_name = request.POST.get('bill_name')
            user_id = request.POST.get('user_id')
            phonepe_id = request.POST.get('phonepe_id')
            amount = request.POST.get('amount')
            Out_phonepe_transition(
                user_id=user_id,
                out_bill_name=bill_name,
                amount=amount,
                phonepe_id=phonepe_id            
                ).save()
            return redirect('/user/out/')
        if 'User_out_bank' in request.POST:
            bill_name = request.POST.get('bill_name')
            user_id = request.POST.get('user_id')
            bank_id = request.POST.get('bank_id')
            amount = request.POST.get('amount')
            User_out_bank(
                user_id=user_id,
                out_bill_name=bill_name,
                amount=amount,
                bank_id=bank_id            
                ).save()
            return redirect('/user/out/')
        
        context={
            'user':user,
            'cash':cash,
            'phonepe':phonepe,
            'bank':bank,
            'cash_amount':Out_transition.objects.filter(user_id=user.id).order_by('-id'),
            'phonepe_transition':Out_phonepe_transition.objects.filter(user_id=user.id).order_by('-id'),
            'bank_transition':User_out_bank.objects.filter(user_id=user.id).order_by('-id'),
}
        return render(request, 'user/out.html', context)
    else:
        return redirect('login')
    
    
def transfer(request):
    if request.session.has_key('user_mobile'):
        user_mobile = request.session['user_mobile']
        user=User.objects.filter(mobile=user_mobile).first()
        cash= User_cash.objects.filter(user_id=user.id).first()
        phonepe= Phonepe.objects.filter(user_id=user.id)
        bank= Bank_account.objects.filter(user_id=user.id)
        if 'User_transfer_cash'in request.POST:
            transfer_to_user_id = request.POST.get('transfer_to_user_id')
            amount = request.POST.get('amount')
            Cash_transfer(
                from_user_id = user.id,
                to_user_id   = transfer_to_user_id,
                amount       = amount, 
            ).save()
            return redirect('transfer')
        if 'User_transfer_cash_to_bank'in request.POST:
            transfer_to_user_bank_id = request.POST.get('transfer_to_user_bank_id')
            amount = request.POST.get('amount')
            Cash_transfer_to_bank(
                from_user_id = user.id,
                to_bank_id   = transfer_to_user_bank_id,
                amount       = amount, 
            ).save()
            return redirect('transfer')
        if 'User_transfer_phonepe'in request.POST:
            from_phonepe_id = request.POST.get('from_phonepe_id')
            transfer_to_user_phonepe_id = request.POST.get('transfer_to_user_phonepe_id')
            amount = request.POST.get('amount')
            Phonepe_transfer(
                from_user_id = user.id,
                from_phonepe_id   = from_phonepe_id,
                to_phonepe_id   = transfer_to_user_phonepe_id,
                amount       = amount, 
            ).save()
            return redirect('transfer')
        if 'User_transfer_bank'in request.POST:
            from_bank_id = request.POST.get('from_bank_id')
            transfer_to_user_bank_id = request.POST.get('transfer_to_user_bank_id')
            amount = request.POST.get('amount')
            Bank_transfer(
                from_user_id = user.id,
                from_bank_id   = from_bank_id,
                to_bank_id   = transfer_to_user_bank_id,
                amount       = amount, 
            ).save()
            return redirect('transfer')
        context={
            'user':user,
            'cash':cash,
            'phonepe':phonepe,
            'bank':bank,
            'cash_amount':Cash_transfer.objects.filter(from_user_id=user.id).order_by('-id'),
            'phonepe_transition':Phonepe_transfer.objects.filter(from_user_id=user.id).order_by('-id'),
            'bank_transition':Bank_transfer.objects.filter(from_user_id=user.id).order_by('-id'),
            'cash_transfer_to_bank':Cash_transfer_to_bank.objects.filter(from_user_id=user.id).order_by('-id'),
        }
        return render(request, 'user/transfer.html', context)
    else:
        return redirect('login')
    
def phonepe_verify(request):
    if request.session.has_key('user_mobile'):
        user_mobile = request.session['user_mobile']
        user=User.objects.filter(mobile=user_mobile).first()
        
        context={
            'user':user,
        }
        return render(request, 'user/phonepe_verify.html', context)
    else:
        return redirect('login')