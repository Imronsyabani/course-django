from django import forms

class SignIN(forms.Form):

    email = forms.EmailField(label="Email",)
    password = forms.CharField(label="Password",)

class SignUP(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email",)
    password = forms.CharField(label="Password",)