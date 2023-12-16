from django import forms


class UserSignup(forms.Form):
    username=forms.CharField(label='نام کاربری')
    useremail=forms.EmailField(label='ایمیل')
    userpassword=forms.CharField(label='رمزعبور')
    userpasswordconfirm=forms.CharField(label='تکرار رمز عبور')
