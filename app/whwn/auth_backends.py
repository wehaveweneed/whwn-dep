from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
from whwn.models import WHWNUser

class WHWNUserAuthBackend(ModelBackend):
    """
    Custom model backend to help django return WHWNUsers on
    `request.user` instead of the standard User provided by
    django.contrib.auth.
    """

    def get_user(self, user_id):
        try:
            return WHWNUser.objects.get(pk=user_id)
        except WHWNUser.DoesNotExist:
            return None
