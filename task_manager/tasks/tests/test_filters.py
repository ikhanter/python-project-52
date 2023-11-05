from django.test import TestCase, Client
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.tasks.filters import TaskFilter


class TestFilter(TestCase):

    def setUp(self):
        self.client = Client()
        self.label1 = Label.objects.create(name='label1')
        self.label2 = Label.objects.create(name='label2')
        self.label3 = Label.objects.create(name='label3')
        self.status1 = Status.objects.create(name='status1')
        self.status2 = Status.objects.create(name='status2')
        self.test_user1 = CustomUser.objects.create_user(
            username='test_user1',
            password='test_pass1',
        )
        self.test_user2 = CustomUser.objects.create_user(
            username='test_user2',
            password='test_pass2',
        )
        self.task1 = Task.objects.create(
            name='task1',
            description='description1',
            status=self.status1,
            executor=self.test_user2,
            creator=self.test_user1,
        )
        self.task1.labels.set([self.label1, self.label2])
        self.task2 = Task.objects.create(
            name='task2',
            description='description2',
            status=self.status2,
            executor=self.test_user1,
            creator=self.test_user2,
        )
        self.task2.labels.set([self.label1, self.label3])
        self.task3 = Task.objects.create(
            name='task3',
            description='description3',
            status=self.status1,
            executor=self.test_user1,
            creator=self.test_user1,
        )
        self.task3.labels.set([self.label2])

    def test_filter(self):
        self.client.login(username='test_user1', password='test_pass1')
        queryset = Task.objects.all()
        test1 = {
            'labels': [
                self.label1.pk,
            ],
            'status': self.status1,
        }
        filtered_queryset = TaskFilter(test1, queryset, user=self.test_user1).qs  # noqa: E501
        self.assertEquals(len(filtered_queryset), 1)
        self.assertIn(self.task1, filtered_queryset)
        test2 = {
                    'self_tasks': True,
                }
        filtered_queryset = TaskFilter(test2, queryset, user=self.test_user1).qs  # noqa: E501
        self.assertEquals(len(filtered_queryset), 2)
        self.assertIn(self.task1, filtered_queryset)
        self.assertIn(self.task3, filtered_queryset)
        test3 = {
            'executor': self.test_user1,
            'self_tasks': True,
        }
        filtered_queryset = TaskFilter(test3, queryset, user=self.test_user1).qs  # noqa: E501
        self.assertEquals(len(filtered_queryset), 1)
        self.assertIn(self.task3, filtered_queryset)
