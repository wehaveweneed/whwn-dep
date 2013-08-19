from django.contrib.auth.models import User
from whwn.models import WHWNUser

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.serializers import Serializer


class TeamAuthorization(Authorization):
    def is_authorized(self, object_list, bundle):
        return object_list.filter(userprofile__team=bundle.request.user.get_profile().team)


class UserResource(ModelResource):
    class Meta:
        queryset = WHWNUser.objects.all()
        resource_name = 'user'
        fields = ['id', 'username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        
        authentication = ApiKeyAuthentication()
        authorization = TeamAuthorization()
        serializer = Serializer(formats=['json'])
