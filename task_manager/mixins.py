from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponseRedirect


class CheckUserMixin(UserPassesTestMixin):

    def test_func(self):
        return self.check_user()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, self.error_message)
        return HttpResponseRedirect(self.no_permission_redirect_url)
