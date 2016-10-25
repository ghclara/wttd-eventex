from django.contrib import admin
from django.utils.timezone import now

from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'cpf',
        'created_at',
        'susbcribed_today',
        'paid',
    )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf')
    list_filter = ('paid', 'created_at')

    def susbcribed_today(self, obj):
        return obj.created_at == now().date()

    susbcribed_today.short_description = 'Inscrição hoje?'
    susbcribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
