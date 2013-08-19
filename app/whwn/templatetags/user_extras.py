from django import template
from whwn.models.user import UserProfile
from django.contrib.auth.models import User
import pdb

register = template.Library()

register.filter('pdb', pdb)
