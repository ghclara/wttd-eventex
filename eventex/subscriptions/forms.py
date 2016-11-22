from django import forms

from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números')

    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 números')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome:')
    cpf = forms.CharField(label='CPF:', validators=[validate_cpf])
    email = forms.CharField(label='Email:', required=False)
    phone = forms.CharField(label='Telefone:', required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name.title()

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou Telefone')

        return self.cleaned_data
