from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.serializers import Serializer
from tastypie.paginator import Paginator
from whwn.api.users import UserResource
from whwn.api.teams import TeamResource

from whwn.models import Message, WHWNUser

class MessageAuthorization(Authorization):
    def is_authorized(self, object_list, bundle):
        return object_list.filter(team=bundle.request.user.get_profile().team)


class MessageAuthorization(Authorization):
    def is_authorized(self, object_list, bundle):
        return object_list.filter(team=bundle.request.user.get_profile().team)


class MessageResource(ModelResource):
    author = fields.ToOneField(UserResource, 'author', null=True, full=True)
    team = fields.IntegerField(attribute="team_id")

    class Meta:
        queryset = Message.objects.order_by('-created_at')
        resource_name = "message"
        excludes = ['flagged', 'deleted', 'updated_at']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        paginator_class = Paginator
        authentication = ApiKeyAuthentication()
        authorization = MessageAuthorization()
        always_return_data = True

    def hydrate_author(self, bundle):
        bundle.obj.author = bundle.request.user
        return bundle

    def hydrate_team(self, bundle):
        bundle.obj.team = bundle.request.user.get_profile().team
        return bundle