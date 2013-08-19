from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse

from registration.forms import RegistrationFormUniqueEmail

from whwn.views.users import (LoginView, LogoutView)
from whwn.register import verify

urlpatterns = patterns("whwn.views.accounts",
            url(r'^login/$', LoginView.as_view(), {}, name="login"),
            url(r'^logout/$', LogoutView.as_view(), {}, name="logout"),
            url(r'^verify/complete/$',
                           direct_to_template,
                           {'template': 'registration/activation_complete.html'},
                           name='registration_activation_complete'),
            url(r'^verify/(?P<activation_key>\w+)/$',
                           verify, 
                           name='registration_activate'),
)
