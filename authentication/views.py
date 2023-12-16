from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from .forms import UserSignup
from . models import CustomUser
def signup(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            useremail=form.cleaned_data['useremail']
            userpassword=form.cleaned_data['userpassword']
            userpassword2=form.cleaned_data['userpasswordconfirm']
            password = passconf(userpassword,userpassword2)
            if password:
                try :
                    new_user=CustomUser(email=useremail , username = username , password = userpassword)
                    new_user.save()
                    return HttpResponseRedirect('/accounts/login/')
                except IntegrityError as e:
                    context={'message':'ایمیل تکراری یا نا معتبر','form': form}
                    form = UserSignup()
                    return render(request, 'account/signup.html', context)


                
    else:
        form = UserSignup()
        return render(request, 'account/signup.html', {'form': form})

def passconf(p , p1):
    if p == p1:
        return True
    else:
        return False
