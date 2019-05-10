import behave
from account import Account
from unittest2 import TestCase

@given(u'an account with a total of money equals to R$ 50')
def step(context):
    account = Account(50)
    context.response = account

@when(u'the account owner attempts to makes a withdraw of R$ {amount}')
def step(context,amount):
    account = context.response
    try:
        context.response = account.withdraw(int(amount))    
    except Exception as error:
        context.response = str(error)

@then(u'the follow message {message} should appear')
def step(context,message):
    if context.response != message:
        raise Exception("Deu ruim")

@when(u'the account owner attempts to makes a deposit of R$ {amount}')
def step(context,amount):
    account = context.response
    try:
        context.response = account.deposit(int(amount))
    except Exception as error:
        context.response = str(error)

@then(u'the current total of money should be {current_total}')
def step(context,current_total):
    if context.response != int(current_total):
        raise Exception("Deu ruim")
    
        





    
    
