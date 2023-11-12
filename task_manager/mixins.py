from task_manager.users.models import CustomUser


class CheckUserForContentMixin:

    def is_user_is_author(
        self,
        user_authorized: CustomUser,
        user_in_content: CustomUser,
    ) -> bool:
        if user_authorized.pk == user_in_content.pk:
            return True
        return False
