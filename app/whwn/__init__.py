from annoying.functions import get_object_or_None

from django.db.models.signals import post_syncdb
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission, Group, User

def add_user_group_and_permission(sender, **kwargs):
    ct = get_object_or_None(ContentType, app_label='whwn', model='item')
    if ct:
        permission = get_object_or_None(Permission, codename="add_item",
                                        content_type=ct)
        if not permission:
            perms = {
                "codename": "add_item", 
                "name": "Can add items",
                "content_type": ct,
            }
            Permission.objects.create(**perms)

        group, created = Group.objects.get_or_create(name='base_users')
        permissions = Permission.objects.filter(content_type=ct)
        group.permissions.add(*permissions)
        users = User.objects.all()
        group.user_set.add(*users)

post_syncdb.connect(add_user_group_and_permission, sender=auth_models)
