from django.conf.urls.defaults import patterns, url
from whwn.views.csv_upload import CSVUploadView
from whwn.views.items import (ItemsView, ItemView, 
                              HeatmapView, HeatmapDataView)

urlpatterns = patterns("whwn.views.items",
      url(r"^fileupload/$", CSVUploadView.as_view(), name = "csv_upload"),
      url(r"^heatmapdisplay/$", HeatmapView.as_view(), name = "heatmap"),
      url(r"^heatmapdisplay/(?P<mode>\w+)+/$", HeatmapView.as_view()),
      url(r"^heatmapdata",HeatmapDataView.as_view(), name = "heatmapdata"),
      url(r"^$", ItemsView.as_view(), name="index"),
)
