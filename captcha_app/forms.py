from django import forms

class CaptchaForm(forms.Form):
    captcha = forms.CharField(max_length=5, required=True, label="Enter CAPTCHA")
