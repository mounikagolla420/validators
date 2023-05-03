from django import forms
from django.core import validators
def check_for_s(value):
    if value[0]=='s':
      raise forms.ValidationError('these is first letter')

def check_for_mail(value):
    if len(value)<20:
        raise forms.ValidationError('these len is short')

class studentform(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_s])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_mail=forms.EmailField()
    course=forms.CharField(max_length=100)
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]/d{9}')])

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_mail']
        if e!=r:
             raise forms.ValidationError('data is not valid')


    #def clean_age(self):
        #a=self.cleaned_data['age']
        #if a<14:
            #raise forms.ValidationError('age is low')

    def botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('not valid')


