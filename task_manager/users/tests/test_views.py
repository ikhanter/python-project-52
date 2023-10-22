from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import CustomUser


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.users_create_url = reverse('users_create')
        self.users_index_url = reverse('users_index')
        self.test_user = CustomUser.objects.create_user(
            username='test_user',
            password='123',
        )
        self.users_update_url = reverse('users_update', args=[self.test_user.pk])  # noqa: E501
        self.users_delete_url = reverse('users_delete', args=[self.test_user.pk])  # noqa: E501

    def test_UsersCreateView_GET(self):
        response = self.client.get(self.users_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_create.html')

    def test_UsersCreateView_POST(self):
        response = self.client.post(self.users_create_url, {
            'first_name': 'test1',
            'username': 'test1',
            'password': 'test1',
            'confirm_password': 'test1',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomUser.objects.get(username='test1').first_name, 'test1')  # noqa: E501

    def test_UsersIndexView_GET(self):
        response = self.client.get(self.users_index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_index.html')

    def test_UsersUpdateView_GET(self):
        # Unauthorized
        response1 = self.client.get(self.users_update_url)
        self.assertEquals(response1.status_code, 302)
        # Authorized
        self.client.login(username="test_user", password="123")
        response2 = self.client.get(self.users_update_url)
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, 'users/users_update.html')

    def test_UsersUpdateView_POST(self):
        self.client.login(username="test_user", password="123")
        response1 = self.client.post(self.users_update_url, {
            'first_name': 'test_user',
            'username': 'test_user',
            'password': 't',
            'confirm_password': 't',
        })
        self.assertEquals(response1.status_code, 200)
        self.assertTemplateUsed(response1, 'users/users_update.html')
        response2 = self.client.post(self.users_update_url, {
            'first_name': 'test_user',
            'username': 'test_user',
            'password': 'test_pass',
            'confirm_password': 'test_pass',
        })
        self.assertEquals(response2.status_code, 302)

    def test_UsersDeleteView_GET(self):
        # Unauthorized
        response1 = self.client.get(self.users_delete_url)
        self.assertEquals(response1.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='123')
        response2 = self.client.get(self.users_delete_url)
        self.assertEquals(response2.status_code, 200)

    def test_UsersDeleteView_POST(self):
        self.client.login(username='test_user', password='123')
        response = self.client.post(self.users_delete_url)
        self.assertEquals(response.status_code, 302)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(username='test_user')
