from django import forms
from .models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount','transaction_type']
        
    def __init__(self,*args,**kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args,**kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput
    
    def save(self,commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposite_amount = 500
        amount = self.cleaned_data.get('amount')
        if amount<min_deposite_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposite_amount} $'
            )
        return amount
    


class WithdrawalForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdrawal_amount = 500
        max_withdrawal_amount = 50000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        
        if amount<min_withdrawal_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdrawal_amount} $'
            )
            
        if amount>max_withdrawal_amount:
             raise forms.ValidationError(
                f'You can withdraw at most {max_withdrawal_amount} $'
            )
        
        if amount>balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )
        
        return amount


class LoanForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        balance = account.balance
        max_loan = balance*2
        amount = self.cleaned_data.get('amount') 
        
        if amount>max_loan:
            raise forms.ValidationError(
                f'You can take loan at most {max_loan} $'
            )
        
        return amount
        
        