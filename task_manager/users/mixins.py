class CheckUserInUsersMixin:

    def check_user(self):
        return self.request.user.pk == self.kwargs['pk']
