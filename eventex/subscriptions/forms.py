from django import forms

from django.core.exceptions import ValidateError


def validate_cpf(value):
    if not value.is_digit():
        raise ValidateError('CPF deve conter apenas números')

    if len(value) != 11:
        raise ValidateError('CPF deve conter 11 números')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome:')
    cpf = forms.CharField(label='CPF:', validators=[validate_cpf])
    email = forms.CharField(label='Email:')
    phone = forms.CharField(label='Telefone:')
