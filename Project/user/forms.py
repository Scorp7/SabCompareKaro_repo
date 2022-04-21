from django import forms
from .models import ContactDetail
from django.forms import widgets


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = ["name", "email", "phone", "message"]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid','placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'emailid','placeholder':'Email*'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone*'}),
            'message': forms.TextInput(attrs={'class':'form-control','id':'passwordid','placeholder':'Message'}),
        }
        
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'message': '',
        }