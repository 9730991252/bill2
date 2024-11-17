from django.db import models

# Create your models here.
class User_type(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)

class User(models.Model):
    user_type=models.ForeignKey(User_type,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField(default=1)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        user = User.objects.filter(status=1).last()
        if User_cash.objects.filter(user_id=user.id).exists():
            pass
        else:
            User_cash(
                user_id=user.id
            ).save()
        
 
class User_cash(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0)
    

class Phonepe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    mobile = models.IntegerField()
    amount = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    
class Bank_account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    bank_name = models.CharField(max_length=100, null=True)
    number = models.IntegerField()
    amount = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    
class Bill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    user_type=models.ForeignKey(User_type,on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    bill_number = models.CharField(max_length=100)
    office_verify_status = models.IntegerField(default=1)
    admin_verify_status = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    pending_amount = models.FloatField()
    pending_amount_status = models.IntegerField(default=1)
    
     
Payment_type = (
    ("1", "In"),
    ("2", "Out"),
)
class Cash_amount(models.Model):
    bill=models.ForeignKey(Bill,on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    payment_type = models.IntegerField()
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        if self.payment_type == 1:
            user_cash = User_cash.objects.filter(user_id=self.bill.user_id).last()
            user_cash.amount += float(self.amount)
            user_cash.save()
            
class Phonepe_transition(models.Model):
    bill=models.ForeignKey(Bill,on_delete=models.CASCADE, null=True)
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    payment_type = models.IntegerField()
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    phonepe=models.ForeignKey(Phonepe,on_delete=models.CASCADE, null=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        if self.payment_type == 1:
            phonepe = Phonepe.objects.filter(id=self.phonepe_id).last()
            phonepe.amount += float(self.amount)
            phonepe.save()
            
class Bank_transition(models.Model):
    bill=models.ForeignKey(Bill,on_delete=models.CASCADE, null=True)
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    payment_type = models.IntegerField()
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    bank=models.ForeignKey(Bank_account,on_delete=models.CASCADE, null=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        if self.payment_type == 1:
            bank = Bank_account.objects.filter(id=self.bank_id).last()
            bank.amount += float(self.amount)
            bank.save()


class Out_transition(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    out_bill_name = models.CharField(max_length=100)
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        self.user_id
        user_cash = User_cash.objects.filter(user_id=self.user_id).last()
        if float(user_cash.amount) > float(self.amount):
            user_cash.amount -= float(self.amount)
            user_cash.save()
            
class Out_phonepe_transition(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    out_bill_name = models.CharField(max_length=100)
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    phonepe=models.ForeignKey(Phonepe,on_delete=models.CASCADE, null=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        user_phonepe = Phonepe.objects.filter(id=self.phonepe_id).last()
        if user_phonepe.amount > float(self.amount):
            user_phonepe.amount -= float(self.amount)
            user_phonepe.save()
            
class User_out_bank(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    out_bill_name = models.CharField(max_length=100)
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    bank=models.ForeignKey(Bank_account,on_delete=models.CASCADE, null=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        user_bank = Bank_account.objects.filter(id=self.bank_id).last()
        if user_bank.amount > float(self.amount):
            user_bank.amount -= float(self.amount)
            user_bank.save()
            

class Cash_transfer(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)    
    to_user=models.ForeignKey(User_cash,on_delete=models.CASCADE, null=True)    
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    to_verify_status = models.IntegerField(default=0)
    cash_remark = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        user_cash = User_cash.objects.filter(user_id=self.from_user_id).last()
        if float(user_cash.amount) > float(self.amount):
            user_cash.amount -= float(self.amount)
            user_cash.save()
            to_user_cash = User_cash.objects.filter(user_id=self.to_user.user_id).last()
            to_user_cash.amount += float(self.amount)
            to_user_cash.save()
             
class Cash_transfer_to_bank(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)    
    to_bank = models.ForeignKey(Bank_account,on_delete=models.CASCADE, null=True) 
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    to_verify_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        user_cash = User_cash.objects.filter(user_id=self.from_user_id).last()
        if float(user_cash.amount) > float(self.amount):
            user_cash.amount -= float(self.amount)
            user_cash.save()
            to_user_bank = Bank_account.objects.filter(id=self.to_bank_id).last()
            to_user_bank.amount += float(self.amount)
            to_user_bank.save()
             
class Phonepe_transfer(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)    
    from_phonepe_id = models.CharField(max_length=100)   
    to_phonepe = models.ForeignKey(Phonepe,on_delete=models.CASCADE, null=True)    
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    to_verify_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        from_phonepe = Phonepe.objects.filter(id=self.from_phonepe_id).last()
        if float(from_phonepe.amount) > float(self.amount):
            from_phonepe.amount -= float(self.amount)
            from_phonepe.save()
            to_user_phonepe = Phonepe.objects.filter(id=self.to_phonepe_id).last()
            to_user_phonepe.amount += float(self.amount)
            to_user_phonepe.save()
        
class Bank_transfer(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)    
    from_bank_id = models.CharField(max_length=100)   
    to_bank = models.ForeignKey(Bank_account,on_delete=models.CASCADE, null=True)    
    amount = models.FloatField()
    self_verify_status = models.IntegerField(default=0)
    office_verify_status = models.IntegerField(default=0)
    admin_verify_status = models.IntegerField(default=0)
    to_verify_status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        from_bank = Bank_account.objects.filter(id=self.from_bank_id).last()
        if float(from_bank.amount) > float(self.amount):
            from_bank.amount -= float(self.amount)
            from_bank.save()
            to_user_bank = Bank_account.objects.filter(id=self.to_bank_id).last()
            to_user_bank.amount += float(self.amount)
            to_user_bank.save()
        