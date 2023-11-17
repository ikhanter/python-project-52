class CheckUserForTasksMixin:

    def check_user(self):
        return self.request.user.pk == self.get_object().creator.pk
