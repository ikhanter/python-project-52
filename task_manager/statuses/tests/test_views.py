from django.test import TestCase, Client
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.statuses_index_url = reverse('statuses_index')
        self.statuses_create_url = reverse('statuses_create')
        self.test_status = Status.objects.create(
            name='test_status',
        )
        self.test_user = CustomUser.objects.create_user(
            username='test_user',
            password='test_pass',
        )
        self.statuses_update_url = reverse('statuses_update', args=[self.test_status.pk])  # noqa: 501
        self.statuses_delete_url = reverse('statuses_delete', args=[self.test_status.pk])  # noqa: 501

    def test_StatusesIndexView_GET(self):
        # Unauthorized
        response = self.client.get(self.statuses_index_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        response = self.client.get(self.statuses_index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('statuses/statuses_index.html')

    def test_StatusesCreateView_GET(self):
        # Unauthorized
        response = self.client.get(self.statuses_create_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        response = self.client.get(self.statuses_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('statuses/statuses_create.html')

    def test_StatusesCreateView_POST(self):
        # Unauthorized
        response = self.client.post(self.statuses_create_url, {
            'name': 'test_status1',
        })
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        # Already exists
        response = self.client.post(self.statuses_create_url, {
            'name': 'test_status',
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Status.objects.all()), 1)
        # New one
        response = self.client.post(self.statuses_create_url, {
            'name': 'test_status2',
        })
        self.assertEquals(len(Status.objects.all()), 2)
        self.assertEquals(response.status_code, 302)

    def test_StatusesUpdateView_GET(self):
        # Unauthorized
        response = self.client.get(self.statuses_update_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        response = self.client.get(self.statuses_update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('statuses/statuses_update.html')

    def test_StatusesUpdateView_POST(self):
        # Unauthorized
        response = self.client.post(self.statuses_update_url, {
            'name': 'test_status_status',
        })
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        response = self.client.post(self.statuses_update_url, {
            'name': 'test_status_status',
        })
        self.assertEquals(Status.objects.get(pk=self.test_status.pk).name, 'test_status_status')  # noqa: 501
        self.assertEquals(response.status_code, 302)

    def test_StatusesDeleteView_GET(self):
        # Unauthorized
        response = self.client.get(self.statuses_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        response = self.client.get(self.statuses_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('statuses/statuses_delete.html')

    def test_StatusesDeleteView_POST(self):
        # Unauthorized
        response = self.client.post(self.statuses_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user', password='test_pass')
        response = self.client.post(self.statuses_delete_url)
        self.assertEquals(len(Status.objects.all()), 0)
        self.assertEquals(response.status_code, 302)
