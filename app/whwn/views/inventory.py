from django.http import Http404
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from haystack.query import SearchQuerySet
import json

from whwn.models import Item
from whwn.api.items import ItemCategoryResource


class InventoryView(TemplateView):
    template_name = 'inventory/index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)

        r = ItemCategoryResource()
        r_list = r.get_object_list(None) # may append `.filter(**kwargs)` like any QuerySet
        r_to_serialize = [r.full_dehydrate(r.build_bundle(obj=obj)) for obj in r_list]
        r_json = r.serialize(None, r_to_serialize, 'application/json')

        context.update({'categories': json.dumps(r_json)})
        return context
