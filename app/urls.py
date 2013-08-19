from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from registration.forms import RegistrationFormUniqueEmail
from whwn.forms.users import NewUserRegistrationForm
from django.contrib import admin
from django.conf import settings

from tastypie.api import Api

from whwn.views.about import AboutView
from whwn.views.users import LoginView
from whwn.views.inventory import InventoryView
from whwn.api.items import ItemResource, ItemCategoryResource
from whwn.api.users import UserResource
from whwn.api.messages import MessageResource
# from whwn.api.teams import TeamResource

admin.autodiscover()

# API Resources
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ItemResource())
v1_api.register(ItemCategoryResource())
v1_api.register(MessageResource())
# v1_api.register(TeamResource())

urlpatterns = patterns('',
    url(r'^v2/', direct_to_template, {'template': 'v2/index.html'}, name='v2'),
    url(r'^$', LoginView.as_view(), {}, name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', AboutView.as_view(), {}, name="about"),
    url(r"^404/$", direct_to_template, {'template': '404.html'}, name='404'),
    url(r"^accounts/", include("whwn.urls.accounts", namespace="accounts",
        app_name="whwn")),
    url(r"^locations/", include("whwn.urls.locations", namespace="locations",
                                app_name="whwn")),
    url(r"^users/", include("whwn.urls.users", namespace="users",
        app_name="whwn")),

    url(r"^accounts/register/$", 'registration.views.register',
        {"form_class": NewUserRegistrationForm,
         "backend": "whwn.register.RegistrationBackend",
         "template_name": "registration/signup.html"}),

    url(r"^inventory", InventoryView.as_view(), name='inventory_list'),
    # Django Registration Backend
    url(r"^accounts/", include('registration.backends.simple.urls')),

    # Django Haystack
    url(r"^search/", include('haystack.urls')),

    # Static
    url(r"^help/$", direct_to_template, {'template': 'help.html'},
        name='help'),
    url(r"^contact/$", direct_to_template, {'template': 'contact.html'},
        name='contact'),
    url(r"^sponsors$", direct_to_template, {'template': 'sponsor.html'},
        name='sponsor'),
    url(r"^privacy/$", direct_to_template, {'template': 'privacy.html'},
        name='privacy'),
    url(r"^legal/$", direct_to_template, {'template': 'legal.html'},
        name='legal'),

    # Tools
    url(r"^tools/", include("tools.urls")),

    # API Endpoints
    url(r'^api/', include(v1_api.urls)),

)

if settings.DEBUG is False:   # if DEBUG is True, will be served automatically
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
