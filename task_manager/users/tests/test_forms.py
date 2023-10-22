from django.forms import ValidationError
from django.test import TestCase
from task_manager.users.forms import UsersCreateForm


class TestForms(TestCase):

    def test_UsersCreateForm_invalid_data(self):
        form1 = UsersCreateForm(data={
            'username': '!@#$%^&*',
            'password': 'test_pass',
            'confirm_password': 'test_pass',
        })
        form1.clean_password()
        self.assertFalse(form1.is_valid())
        form2 = UsersCreateForm(data={
            'username': 'test_user',
            'password': 'test_pass',
            'confirm_password': 'test_pass2',
        })
        with self.assertRaises(ValidationError):
            form2.clean_password()
