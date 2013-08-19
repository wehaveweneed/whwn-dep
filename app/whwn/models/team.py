from django.db import models
from django.contrib.auth.models import User
from whwn.models.abstract import Timestamps, Locatable
from whwn.models import Item, WHWNUser

class Team(Timestamps, Locatable):
    # The foreign-key references below are strings, because the relationships
    # must be determined at runtime to prevent circular dependencies

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    primary_user = models.ForeignKey(User,
            related_name="primary_user", null=True)

    class Meta:
        app_label = "whwn"

    def __unicode__(self):
        return self.name


    def items(self):
        """
        :param items: Items that belong to this team.
        :returns: 
        """
        return Item.objects.filter(sku__team=self)

    def members(self):
        """
        :returns: A Queryset of Users that belong in this team
        """

        return WHWNUser.objects.filter(userprofile__team=self)
