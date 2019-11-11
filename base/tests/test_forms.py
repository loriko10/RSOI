from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from base.forms import LoginForm

class LoginFormTest(TestCase):

    def test_login_form_username_field(self):
        form = LoginForm()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'Username')

    def test_login_form_password_field(self):
        form = LoginForm()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Password')

    def test_login_form_max_length_field(self):
        form = LoginForm()
        self.assertTrue(form.fields['password'].widget.attrs['maxlength'], 30)

    def test_login_form_valid(self):
        form = LoginForm()
        form_widget_attrs = {'class': 'form-control', 'name': 'username', '1': '1'}
        form.fields['password'].widget.attrs = form_widget_attrs
        self.assertFalse(form.is_valid())
