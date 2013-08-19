from django.conf.urls.defaults import patterns, url
from whwn.views.users import (SettingsView, UpdateEmailView,
                              UpdatePasswordView, 
                              UpdateLocationView,
                              UpdateTeamView,
                              DeleteLocationView,
                              AddLocationView)

# These routes are all within whwn.users.views
urlpatterns = patterns("whwn.views.users",
    url(r"^settings/$", SettingsView.as_view(), {}, name="settings"),
    url(r"^settings/email/update$", UpdateEmailView.as_view()),
    url(r"^settings/team/update$", UpdateTeamView.as_view()),
    url(r"^settings/teams$", "teams_autocomplete", name="teams_autocomplete"),
    url(r"^settings/password/update$", UpdatePasswordView.as_view()),
    url(r"^settings/locations/update$", UpdateLocationView.as_view()),
    url(r"^settings/locations/delete$", DeleteLocationView.as_view()), 
    url(r"^settings/locations/add$", AddLocationView.as_view()), 


    url(r"^requests/$", "requests", name="requests"),
    # url(r"^forgot_password/$", "forgot_password", name="forgot_password"),
    url(r"^(?P<id>\d+)$", "profile", name="profile"),
    url(r"^messages/$", "user_messages", name="user_messages"),
    url(r"^me$", "me", name="me"),
    url(r"^unread_count/(?P<user>\w+)+/$", "unread_count", name="unread_count"),
)

# This is a library function we're using for logout
urlpatterns += (url(r"^logout/$", "django.contrib.auth.views.logout", name="logout"),)
