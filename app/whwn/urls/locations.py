from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("whwn.views.locations",
            url(r"^(?P<sub_location>[a-zA-Z]+)/$", "locations", name="sub_location"),
            url(r"^(?P<sub_location>[a-zA-Z]+)/(?P<model>[a-zA-Z]+)/$", "locations", name="model_location"),
            url(r"^(?P<sub_location>[a-zA-Z]+)/(?P<model>[a-zA-Z]+)/(?P<category>[a-zA-Z]+)", "locations", name="category_location"),
            url(r"^$", "locations", name="all_locations"))
