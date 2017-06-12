from django.core import mail
from django.test import TestCase


class SubcribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Vicente Luz', cpf='12345678911',
                    email='vicente@frigotil.com.br', phone='86-98822-1812')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscript_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_form(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'vicente@frigotil.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Vicente Luz',
            '12345678911',
            'vicente@frigotil.com.br',
            '86-98822-1812'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
