from django.test import TestCase

from django.shortcuts import resolve_url


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        '''GET /must return status code 200
        '''
        self.assertEqual(self. response.status_code, 200)

    def test_template(self):
        '''Must use index.html
        '''
        self.assertTemplateUsed(self. response, 'index.html')
