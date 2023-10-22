from django.test import TestCase
from task_manager.users.models import CustomUser
import datetime, time  # noqa: E401


class TestModels(TestCase):

    def setUp(self):
        self.test_user = CustomUser.objects.create_user(
            first_name='test_first',
            last_name='test_last',
            username='test_user',
            password='test_pass',
        )

    def test_CustomUser_created_updated_time(self):
        creation = datetime.datetime.now().strftime('%H:%M:%S')
        self.assertEquals(self.test_user.created_at.strftime('%H:%M:%S'), creation)  # noqa: E501
        time.sleep(3)
        self.test_user.first_name = 'new_test_first'
        self.test_user.save()
        update = datetime.datetime.now().strftime('%H:%M:%S')
        self.assertEquals(self.test_user.updated_at.strftime('%H:%M:%S'), update)  # noqa: E501
        self.assertEquals(self.test_user.first_name, 'new_test_first')
