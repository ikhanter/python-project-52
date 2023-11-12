from django.test import TestCase, Client
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.tasks_index_url = reverse('tasks_index')
        self.tasks_create_url = reverse('tasks_create')
        self.test_status1 = Status.objects.create(
            name='test_status1',
        )
        self.test_status2 = Status.objects.create(
            name='test_status2',
        )
        self.test_user1 = CustomUser.objects.create_user(
            first_name='test',
            last_name='test',
            username='test_user1',
            password='test_pass1',
        )
        self.test_user2 = CustomUser.objects.create_user(
            first_name='test',
            last_name='test',
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
            creator=self.test_user1,
            executor=self.test_user2,
        )
        self.test_task.labels.set([self.test_label1, self.test_label2])
        self.tasks_show_url = reverse(
            'tasks_show',
            args=[self.test_task.pk],
        )
        self.tasks_update_url = reverse(
            'tasks_update',
            args=[self.test_task.pk],
        )
        self.tasks_delete_url = reverse(
            'tasks_delete',
            args=[self.test_task.pk],
        )

    def test_TasksIndexView_GET(self):
        # Unauthorized
        response = self.client.get(self.tasks_index_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.get(self.tasks_index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('tasks/tasks_index.html')

    def test_TasksCreateView_GET(self):
        # Unauthorized
        response = self.client.get(self.tasks_create_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.get(self.tasks_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('tasks/tasks_create.html')

    def test_TasksCreateView_POST(self):
        # Unauthorized
        response = self.client.post(
            self.tasks_create_url,
            {
                'name': 'test_task2',
                'description': 'test_description2',
                'status': self.test_status1.id,
                'executor': self.test_user2.id,
            },
        )
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        # Already exists
        response = self.client.post(
            self.tasks_create_url,
            {
                'name': 'test_task',
                'description': 'test_description',
                'status': self.test_status1.id,
                'executor': self.test_user2.id,
                'labels': [self.test_label1.id, self.test_label2.id],
            },
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Task.objects.all()), 2)
        # New one
        response = self.client.post(
            self.tasks_create_url,
            {
                'name': 'test_task2',
                'description': 'test_description2',
                'status': self.test_status1.id,
                'executor': self.test_user2.id,
                'labels': [self.test_label1.id],
            },
        )
        self.assertEquals(len(Task.objects.all()), 3)
        self.assertEquals(response.status_code, 302)

    def test_TasksUpdateView_GET(self):
        # Unauthorized
        response = self.client.get(self.tasks_update_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.get(self.tasks_update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('tasks/tasks_update.html')

    def test_TasksUpdateView_POST(self):
        # Unauthorized
        response = self.client.post(
            self.tasks_update_url,
            {
                'name': 'test_task_changed',
                'description': 'test_description_changed',
                'status': self.test_status2.id,
                'executor': self.test_user1.id,
                'labels': [self.test_label1.id],
            },
        )
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.post(
            self.tasks_update_url,
            {
                'name': 'test_task_changed',
                'description': 'test_description_changed',
                'status': self.test_status2.id,
                'executor': self.test_user1.id,
                'labels': [self.test_label1.id],
            },
        )
        self.assertEquals(
            Task.objects.get(pk=self.test_task.pk).name,
            'test_task_changed',
        )
        self.assertEquals(
            Task.objects.get(pk=self.test_task.pk).description,
            'test_description_changed',
        )
        self.assertEquals(
            Task.objects.get(pk=self.test_task.pk).status.name,
            'test_status2',
        )
        self.assertEquals(
            Task.objects.get(pk=self.test_task.pk).executor.username,
            'test_user1',
        )
        self.assertEquals(
            len(Task.objects.get(pk=self.test_task.pk).labels.all()),
            1,
        )
        self.assertEquals(response.status_code, 302)

    def test_TasksDeleteView_GET(self):
        # Unauthorized
        response = self.client.get(self.tasks_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.get(self.tasks_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('tasks/tasks_delete.html')

    def test_TasksDeleteView_POST(self):
        # Unauthorized
        response = self.client.post(self.tasks_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.post(self.tasks_delete_url)
        self.assertEquals(len(Task.objects.all()), 0)
        self.assertEquals(response.status_code, 302)

    def test_TasksView_GET(self):
        # Unauthorized
        response = self.client.post(self.tasks_delete_url)
        self.assertEquals(response.status_code, 302)
        # Authorized
        self.client.login(
            username='test_user1',
            password='test_pass1',
        )
        response = self.client.get(self.tasks_show_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('tasks/tasks_show.html')
