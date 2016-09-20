from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string

from eventex import settings

from .forms import SubscriptionForm


def subscribe(request):
    context = {}
    context['form'] = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                'subscriptions/subscription_form.html',
                {'form': form}
            )

        body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)

        send_mail(
            'Confirmação de Inscrição',
            body,
            settings.DEFAULT_FROM_EMAIL,
            [form.cleaned_data['email']],
        )

        messages.success(request, 'Inscrição realizada com sucesso!')
        return HttpResponseRedirect('/inscricao/')
    return render(request, 'subscriptions/subscription_form.html', context)
