from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.tasks.models import Task


class CheckUserMixin(LoginRequiredMixin):

    def check_user(self, user, pk):
        if user.pk == pk:
            self.is_user_is_author = True
        else:
            self.is_user_is_author = False


class CheckUserForUsersMixin(CheckUserMixin):

    def dispatch(self, request, *args, **kwargs):
        self.check_user(request.user, kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)


class CheckUserForTasksMixin(CheckUserMixin):

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        self.check_user(request.user, task.creator.pk)
        return super().dispatch(request, *args, **kwargs)
