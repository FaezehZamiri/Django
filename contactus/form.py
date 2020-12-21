from . import models
from django import forms

class CreateFormR(forms.ModelForm):
    class Meta:
        model=models.requestform
        fields=['name','number','email','idcode','cardnumber','pay']

class CreateForm(forms.ModelForm):
    class Meta:
        model=models.record
        fields=['name','number','email','body']
