# forms.py
from django import forms

class InputForm(forms.Form):
    number = forms.IntegerField(label='Enter your number')
    string = forms.CharField(label='Hello please add your name:')
