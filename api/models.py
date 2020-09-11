from django.db import models
from django.contrib.auth.models import User

# from django.core.validators import MaxLengthValidator, MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, unique=True,
                                related_name = 'user')
    facebook_user = models.CharField(max_length=250, blank=True, null=True, unique=True )
    phone = models.CharField( blank=True, unique=True, null=True, max_length=20)
    profile = models.CharField(max_length=250, blank=True, null=True, unique=True )


    def __str__(self):
        """one-line docstring for representing the Profile object."""
        return f'{self.user.first_name}'




class Loan_Record(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='record')
    due_date=models.DateField()
    created=models.DateField(auto_now_add=True)
    amount=models.IntegerField()
    interest_rate=models.CharField(max_length=10 , blank=True,null=True)
    paid=models.BooleanField(default=False)
    lender=models.BooleanField(default=True)
    description=models.TextField()
    balance_to_pay=models.IntegerField(blank=True,null=True)




    def __str__(self):
       """one-line docstring for representing the L object."""
       return self.description
