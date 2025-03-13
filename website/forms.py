from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20, required=False)
    subject = forms.CharField(max_length=100)
    budget = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)
