from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.gis.db import models
from registration.signals import user_registered

from annoying.functions import get_object_or_None
from registration.models import RegistrationProfile
from tastypie.models import create_api_key

from whwn.models import Message, Item, WHWNUser
from whwn.models.abstract import Timestamps, Locatable


class UserProfile(Timestamps, Locatable):

    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    team = models.ForeignKey("whwn.Team", null=True)

    class Meta:
        app_label = "whwn"

    def __unicode__(self):
        return "%(username)s" % {'username': self.user.username}

    def save(self, *args, **kwargs):
        """
        We want to force update for existing users
        This was used to address testing issues where we would be attempting
        to insert existing users onto existing profiles instead of updating
        """
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.id = existing.id  # force update instead of insert
            kwargs['force_insert'] = False
            kwargs['force_update'] = True
        except UserProfile.DoesNotExist:
            pass

        models.Model.save(self, *args, **kwargs)


    def send_forgot_password(self, pw):
        message = NotificationMessage(
            notify_type=NotificationMessage.FORGOTTEN_PASSWORD,
            message="""Your temporary password is %s. You can use this
                       password to sign in and change your password
                       from the account settings page""" % (pw),
            sender=self.user,
            type=Message.EMAIL)
        message.send()

    def send_change_password(self):
        message = NotificationMessage(
            notify_type=NotificationMessage.CHANGE_PASSWORD,
            message="""This email is to confirm that you have recently
                       updated your account password.""",
            sender=self.user,
            type=Message.EMAIL
        )
        message.send()


    def resend_activation(self):
        # TODO: Use message class
        reg_profile = get_object_or_None(RegistrationProfile, user=self.user)
        if reg_profile:
            if reg_profile.activation_key != 'ALREADY_ACTIVATED':
                site = Site.objects.get(id=settings.SITE_ID)
                reg_profile.send_activation_email(site)
                return True
        return False

def create_profile(sender, **kw):
    user = kw["instance"]
    group = get_object_or_None(Group, name='base_users')
    if kw["created"]:
        obj, created = UserProfile.objects.get_or_create(user=user)
        if group:
            group.user_set.add(user)

def activate_user(sender, user, request, **kwargs):
    """ Activate user """
    user.is_active = True
    user.save()
    profile = user.get_profile()
    profile.activation_key = RegistrationProfile.ACTIVATED
    profile.save()
    return user

def send_verification_email(user, request, **kwargs):
    from registration.models import RegistrationProfile
    from django.contrib.sites.models import RequestSite
    profile = RegistrationProfile.objects.create_profile(user)
    site = RequestSite(request)

def beta_test_email(user):
    import subprocess
    import json
    from settings.common import project
    from whwn.beta_test_items import beta_test_items
    message_front = """Hello Participant!,\n\nThank you for participating in
                       our usability test!\nHere are your instructions:\n\n
                       Below you will see a list of have's and needs. Your
                       goal is to get rid of all your 'haves' and find all
                       your 'needs'. Since we don't actually have these items,
                       you will 'get' an item by getting the requester's ID number.
                       \n\nItem the items you have, and then start looking for
                       items you need. Once you find them, request them from
                       the requester. Ask them if they still have the item, and if
                       they do, ask them for their ID number. Remember, you
                       only have ONE of each item so you cannot give an item
                       away multiple times.\n\n_____________"""
    message_end = """-------------\n\nOnce you have completed your task, fill
                     out the survey here\nhttps://docs.google.com/spreadsheet/viewform?formkey=dDRZR0FxVkMzSHlSamNjMnVXNFhNX0E6MQ#gid=0\n\n
                     If you need help, you can reach us online here\nhttps://www.hipchat.com/gTHsriAxV\n
                     Thanks Again,\n-the team"""

    out = beta_test_items()

    message_body = "ID: %s" % (out['name'])
    message_body += "\nHaves:\n"
    for have in out["haves"]:
        message_body += "%s" % (have)

    message_body += "\nNeeds:\n"
    for have in out["needs"]:
        message_body += "%s" % (have)

    instructions = "%s\n%s\n%s" % (message_front, message_body, message_end)

    message = NotificationMessage(sender=user,
                                  notify_type=NotificationMessage.BETA_TEST,
                                  contents=instructions)
    message.send()

post_save.connect(create_profile, sender=User, dispatch_uid="users-profilecreation-signal")
post_save.connect(create_api_key, sender=User)
user_registered.connect(activate_user)
user_registered.connect(send_verification_email)

class EmailSender:
    MESSAGES = 'messages@wehave-weneed.org'
    INVENTORY = 'inventory@wehave-weneed.org'
    REQUESTS = 'requests@wehave-weneed.org'
    ADMIN = 'admin@wehave-weneed.org'
    FEEDBACK = 'feedback@wehave-weneed.org'
