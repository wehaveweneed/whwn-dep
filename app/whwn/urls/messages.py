from django.conf.urls.defaults import patterns, url
#from whwn.views.messages import ConversationListView, ConversationView, CreateConversationView

urlpatterns = patterns("whwn.views.messages",
            #url(r"^$", ConversationListView.as_view(), name="index"),
            #url(r"^(?P<id>\d+)+/$", ConversationView.as_view()),
            #url(r"^(?P<id>\d+)/?P<slug>.+/$", ConversationView.as_view())
            )
