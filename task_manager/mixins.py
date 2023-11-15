from django.contrib.auth.mixins import UserPassesTestMixin
from task_manager.tasks.models import Task
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect


class CheckUserMixin(UserPassesTestMixin):

    def check_for_user(self, request, *args, **kwargs):
        if request.user.pk == kwargs['pk']:
            self.is_user_is_creator = True
        else:
            self.is_user_is_creator = False

    def check_for_task(self, request, *args, **kwargs):
        if request.user.pk == Task.objects.get(pk=kwargs['pk']).creator.pk:
            self.is_user_is_creator = True
        else:
            self.is_user_is_creator = False

    def test_func(self):
        if self.is_user_is_creator:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        match self.request.path.split('/')[1]:
            case 'users':
                self.check_for_user(request, *args, **kwargs)
            case 'tasks':
                self.check_for_task(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        match self.request.path.split('/')[1]:
            case 'users':
                return HttpResponseRedirect(reverse_lazy('users_index'))
            case 'tasks':
                return HttpResponseRedirect(reverse_lazy('tasks_index'))
