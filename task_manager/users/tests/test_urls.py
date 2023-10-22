from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task_manager.users.views import UsersIndexView, \
    UsersCreateView, UsersDeleteView, UsersUpdateView


class UrlsTestCase(SimpleTestCase):

    def test_UsersCreate_is_resolved(self):
        url = reverse('users_create')
        self.assertEquals(resolve(url).func.view_class, UsersCreateView)

    def test_UsersIndex_is_resolved(self):
        url = reverse('users_index')
        self.assertEquals(resolve(url).func.view_class, UsersIndexView)

    def test_UsersUpdate_is_resolved(self):
        url = reverse('users_update', args=[1])
        self.assertEquals(resolve(url).func.view_class, UsersUpdateView)

    def test_UsersDelete_is_resolved(self):
        url = reverse('users_delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, UsersDeleteView)
