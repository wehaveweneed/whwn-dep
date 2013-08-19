from annoying.decorators import render_to
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.contrib import messages
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.views.generic import (ListView, CreateView, View, UpdateView,
                                  TemplateView, DeleteView)
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import csv
import logging
import itertools

from whwn.models import Item, ItemCategory
from whwn.forms.items import EditItemForm, DeleteForm, UploadFileForm, CreateItemForm
from whwn.models import UserProfile, Item


class HeatmapView(TemplateView):

    """ This view displays an interface for the user to choose the heatmap that
        she wants rendered
    """
    template_name = "items/heatmap.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HeatmapView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(HeatmapView, self).get_context_data(**kwargs)
        context['categories'] = ItemCategory.objects.all()
        context['mode'] = kwargs.get('mode', 'standard')
        return context


class HeatmapDataView(View):
  
    """ This returns data about items, which is used for rendering the heatmap.
    """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        from haystack.query import SearchQuerySet
        from haystack.utils.geo import Point

        items_query = SearchQuerySet().models(Item)\
                        .filter(is_needed = True)\
                        .exclude(location = None)


        # DB / Business Logic #

        def filter_by_name(items_query, name):
            return items_query.auto_query(name)

        def filter_by_bounds(items_query, bounds):
            point1 = Point(bounds[1], bounds[0])
            point2 = Point(bounds[3], bounds[2])
            return items_query.within("location", point1, point2)

        def filter_by_minimum_itemed_date(items_query, timestamp):
            from datetime import datetime
            return items_query.filter(itemed_date__gte =
                    datetime.fromtimestamp(timestamp))
            
        def filter_by_maximum_itemed_date(items_query, timestamp):
            from datetime import datetime
            return items_query.filter(itemed_date__lte =
                    datetime.fromtimestamp(timestamp))

        def filter_by_category(items_query, category_id):
            from datetime import datetime
            return items_query.filter(category = category_id)

        def jsonify(items_query):
            json = {}
            json['items'] = [{'id':  result.object.item_id,
                              'lat': result.object.location.latitude,
                              'lon': result.object.location.longitude} for result in
                              items_query]
            return json


        # Request Handling #

        if "name" in request.GET:
            items_query = filter_by_name(items_query, request.GET["name"])

        bounds = [ float(request.GET[bound]) for bound in
                   ["northEastLat","northEastLon","southWestLat","southWestLon"] if
                   bound in request.GET ] 

        if (len(bounds) == 4):
            items_query = filter_by_bounds(items_query, bounds)

        if "since" in request.GET:
            items_query = filter_by_minimum_itemed_date(items_query, int(request.GET["since"]))

        if "until" in request.GET:
            items_query = filter_by_maximum_itemed_date(items_query, int(request.GET["until"]))

        if "category" in request.GET:
            items_query = filter_by_category(items_query, request.GET["category"])

        json = jsonify(items_query)

        return HttpResponse(simplejson.dumps(json), mimetype="application/json")
