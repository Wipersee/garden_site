from django import forms
from django.core.exceptions import ValidationError
import re

def validate_phone(value):
    res = re.match(r'^\+380[0-9]{9}$', value)
    if res == None:
        raise ValidationError(
            ('%(value)s is not a valid phone number'),
            params={'value': value},
        )

class OrderForm(forms.Form):
	client_name_field = forms.CharField(label=(u'Ім\'я'), max_length=30)
	phone_field = forms.CharField(label=(u'Телефон'), max_length=30,validators=[validate_phone])
