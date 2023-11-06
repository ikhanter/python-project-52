from django.test import TestCase, Client
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.labels_index_url = reverse('labels_index')
        self.labels_create_url = reverse('labels_create')
        self.test_status1 = Status.objects.create(
            name='test_status1',
        )
        self.test_status2 = Status.objects.create(
            name='test_status2',
        )
        self.test_user1 = CustomUser.objects.create_user(
            first_name='test1',
            last_name='test1',
            username='test_user1',
            password='test_pass1',
        )
        self.test_user2 = CustomUser.objects.create_user(
            first_name='test2',
            last_name='test2',
            username='test_user2',
            password='test_pass2',
        )
        self.test_label1 = Label.objects.create(
            name='test_label1',
        )
        self.test_label2 = Label.objects.create(
            name='test_label2',
        )
        self.test_label3 = Label.objects.create(
            name='test_label3',
        )
        self.test_task = Task.objects.create(
            name='test_task',
            description='test_description',
            status=self.test_status1,
            executor=self.test_user2,
            creator=self.test_user1,
        )
        self.test_task.labels.set([self.test_label1, self.test_label2])
        self.labels_update_url = reverse('labels_update', args=[self.test_label1.pk])  # noqa: 501
        self.labels_delete_url = reverse('labels_delete', args=[self.test_label1.pk])  # noqa: 501
        self.labels_delete_url_empty = reverse('labels_delete', args=[self.test_label3.pk])  # noqa: 501

    def test_LabelsIndexView_GET(self):
        # Unauthorized
        response = self.client.get(self.labels_index_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        response = self.client.get(self.labels_index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('labels/labels_index.html')

    def test_LabelsCreateView_GET(self):
        # Unauthorized
        response = self.client.get(self.labels_create_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        response = self.client.get(self.labels_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('labels/labels_create.html')

    def test_LabelsCreateView_POST(self):
        # Unauthorized
        response = self.client.post(self.labels_create_url, {
            'name': 'new_test_label',
        })
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        # Already exists
        response = self.client.post(self.labels_create_url, {
            'name': 'test_label1',
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Label.objects.all()), 3)
        # New one
        response = self.client.post(self.labels_create_url, {
            'name': 'new_test_label',
        })
        self.assertEquals(len(Label.objects.all()), 4)
        self.assertEquals(response.status_code, 302)

    def test_LabelsUpdateView_GET(self):
        # Unauthorized
        response = self.client.get(self.labels_update_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        response = self.client.get(self.labels_update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('labels/labels_update.html')

    def test_LabelsUpdateView_POST(self):
        # Unauthorized
        response = self.client.post(self.labels_update_url, {
            'name': 'test_label1_updated',
        })
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        response = self.client.post(self.labels_update_url, {
            'name': 'test_label1_updated',
        })
        self.assertEquals(Label.objects.get(pk=self.test_label1.pk).name, 'test_label1_updated')  # noqa: 501
        self.assertEquals(response.status_code, 302)

    def test_LabelsDeleteView_GET(self):
        # Unauthorized
        response = self.client.get(self.labels_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        response = self.client.get(self.labels_delete_url_empty)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('labels/labels_delete.html')
        response = self.client.get(self.labels_delete_url)
        self.assertEquals(response.status_code, 302)

    def test_LabelsDeleteView_POST(self):
        # Unauthorized
        response = self.client.post(self.labels_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(username='test_user1', password='test_pass1')
        # Has linked task
        response = self.client.post(self.labels_delete_url)
        self.assertEquals(len(Label.objects.all()), 3)
        # Has not linked task
        self.test_task.delete()
        response = self.client.post(self.labels_delete_url_empty)
        self.assertEquals(len(Label.objects.all()), 2)
        self.assertEquals(response.status_code, 302)
