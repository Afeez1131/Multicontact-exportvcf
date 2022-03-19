from django import forms


class ContactForm(forms.Form):
    contacts = forms.CharField(max_length=2000)
