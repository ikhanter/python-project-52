class CheckUserForTasksMixin:

    def check_user(self):
        if self.request.user.pk == self.get_object().creator.pk:
            return True
        return False
