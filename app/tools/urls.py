from django.conf.urls.defaults import patterns, url, include
from tools.views import ToolsIndexView, MatchQCListView, MatchQCHomeView

urlpatterns = patterns('tools',
    url(r'^$', ToolsIndexView.as_view(), name='tools_home'),
    url(r'^matchqc/matches$', MatchQCListView.as_view()),
    url(r'^matchqc', MatchQCHomeView.as_view()),
)
