from django import forms
from django.core.exceptions import ValidationError

from .validators import validate_cpf

from .models import Subscription


class SubscriptionOldForm(forms.Form):
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


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone', )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name.title()

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou Telefone')

        return self.cleaned_data
