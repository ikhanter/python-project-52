class CheckUserInUsersMixin:

    def check_user(self):
        if self.request.user.pk == self.kwargs['pk']:
            return True
        return False
