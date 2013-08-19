from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from whwn.models import Team


class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = "Team"
        authorization = Authorization()
