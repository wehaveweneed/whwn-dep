from django.utils import simplejson
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, ListView
from whwn.models import Item
from django.core.paginator import Paginator, Page


class ToolsIndexView(TemplateView):
    template_name = 'tools/index.html'


class MatchQCHomeView(TemplateView):
    """
    Homepage of the Matching Quality Control Application
    """
    template_name = 'tools/matchqc/home.html'


class MatchQCListView(ListView):
    """
    Lists PER_PAGE items with their matches.
    Calls matches() from the Item model.
    Returns matches in JSON format.
    """
    queryset = Item.objects.all()
    paginate_by = 5
    context_object_name = "item_matches"

    def get_context_data(self, **kwargs):
        c = super(MatchQCListView, self).get_context_data(**kwargs)
        c['item_matches'] = [{'item': x, 
                              'matches': [y.object for y in x.matches()]} 
                              for x in c['item_matches']]
        del c['object_list']
        return c

    def render_to_response(self, context, **response_kwargs):
        print context
        return HttpResponse(simplejson.dumps(context, default=self.encode_matches),
                            mimetype='application/json')

    def encode_matches(self, obj):
        """
        Writing our own JSON Encoder so simplejson understands how to serialize
        different objects. It doesn't know how to do this by default, and will
        otherwise return a TypeError.
        """
        if isinstance(obj, Paginator):
            return { 'num_pages': obj.num_pages,
                     'count': obj.count }
        elif isinstance(obj, Page):
            return { 'number': obj.number,
                     'has_next': obj.has_next(),
                     'has_previous': obj.has_previous(),
                     'next_page_number': obj.next_page_number(),
                     'previous_page_number': obj.previous_page_number() }
        elif isinstance(obj, Item):
            return { 'name': obj.name,
                     'amount': obj.amount,
                     'description': obj.description }
        elif isinstance(obj, list):
            return [simplejson.dumps(x, default=self.encode_matches) for x in obj]
        else:
            raise TypeError(repr(obj) + " is not JSON serializable.")
