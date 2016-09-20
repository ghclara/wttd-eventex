from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class Subscriptions(TestCase):

    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        '''GET /inscricao/ must return status code 200
        '''
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        '''Must use subscriptions/subscription_form.html
        '''
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        '''Html contain tags
        '''

        tags = (
            ('<form'),
            ('<input'),
        )

        for text in tags:
            with self.subTest():
                self.assertContains(self.response, text)

    def test_csrf(self):
        '''Html must contain csrf
        '''
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have subscription form
        '''
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        '''Form must have 4 fields
        '''
        form = self.response.context['form']
        self.assertSequenceEqual(list(form.fields), ['name', 'cpf', 'email', 'phone'])
