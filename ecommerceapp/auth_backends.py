from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuthBackend(ModelBackend):
    """
    Authenticate using email instead of username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Lookup user by email
            if user.check_password(password):  # Verify password
                return user
        except User.DoesNotExist:
            return None
        return None
