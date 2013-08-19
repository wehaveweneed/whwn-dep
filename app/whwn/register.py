from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login

from registration import signals
from registration.backends.simple import SimpleBackend
from registration.backends.default import DefaultBackend
from registration.backends import get_backend
from registration.models import RegistrationProfile
from whwn.models import UserProfile
from whwn.models import Team

class RegistrationBackend(SimpleBackend):

    def register(self, request, **kwargs):
        user = super(RegistrationBackend, self).register(request, **kwargs)
        user.profile = UserProfile(user=user)
        if not user.profile.email_verified:
            user.profile.email_verified = True

        if kwargs.get("join_team"):
            user.profile.team = kwargs["join_team"]
            user.profile.save()
        elif kwargs.get("new_team"):
            team = Team(name=kwargs["new_team"])
            team.save()
            user.profile.team = team
            user.profile.save()
            team.primary_user = user
            team.save()
        else:
            redirect(reverse('home'))

        user.save()
        return user

    def activate(self, request, **kwargs):
        activation_key = kwargs['activation_key']
        activated = RegistrationProfile.objects.activate_user(activation_key)
        if activated:
            signals.user_activated.send(sender=self.__class__,
                                        user=activated,
                                        request=request)
        return activated

    def post_registration_redirect(self, request, user):
        return ('inventory_list', (), {})

    def post_activation_redirect(self, request, user):
        return ('inventory_list', (), {})

def verify(request, **kwargs):

    backend = 'whwn.register.RegistrationBackend'
    backend = get_backend(backend)
    user = backend.activate(request, **kwargs)

    if user:
        backend.post_activation_redirect(request, user)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)

            
        return redirect(reverse('inventory_list'))
    else:
        return redirect(reverse('home'))


