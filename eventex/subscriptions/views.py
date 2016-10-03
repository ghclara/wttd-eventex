from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Subscription
from .forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(
            request,
            'subscriptions/subscription_form.html',
            {'form': form}
        )

    obj = Subscription.objects.create(**form.cleaned_data)

    # send email
    _send_mail(
        'Confirmação de Inscrição',
        settings.DEFAULT_FROM_EMAIL,
        obj.email,
        'subscriptions/subscription_email.txt',
        {'subscription': obj}
    )

    return HttpResponseRedirect('/inscricao/{}'.format(obj.pk))


def new(request):
    return render(
        request,
        'subscriptions/subscription_form.html',
        {'form': SubscriptionForm()}
    )


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(
        request,
        'subscriptions/subscription_detail.html',
        {'subscription': subscription}
    )


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send_mail(subject, body, from_, [from_, to])
