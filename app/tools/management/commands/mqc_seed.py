from __future__ import print_function
from django.core.management.base import NoArgsCommand, CommandError
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.db.utils import IntegrityError
from whwn.models import Item, ItemCategory, Location
from factories import ItemFactory, LocationFactory
import random
import json
import datetime
from annoying.functions import get_object_or_None
from pprint import pprint
from settings.common import project
from factories import (UserFactory, LocationFactory, ItemCategoryFactory,
                       ItemFactory, UserProfileFactory, MessageFactory,
                       ConversationFactory, ErrorMessageFactory)


class Command(NoArgsCommand):

    # handle_noargs
    #
    # Method gets called when this command is called through
    # the django provided management system.
    def handle_noargs(self, **options):

        print("")
        print(">> Generate test items <<")
        print("")

        data = self.load_json(project('tools/fakeitems.json'))
        #user = self.get_random_model_instance(User)

        date=datetime.datetime.now()
        print("Creating items...")
        for fake_item in data['items']:
            if fake_item['is_needed']:
                item_type = 'need'
                if get_object_or_None(User, username='lewisf'):
                  user = User.objects.get(username='lewisf')
                else:
                  user = UserFactory.create(username='lewisf')
            else:
                item_type = 'have'
                if get_object_or_None(User, username='j8ngo'):
                  user = User.objects.get(username="j8ngo")
                else:
                  user = UserFactory.create(username='j8ngo')        
                
            try:
                loc = random.choice(Location.objects.filter(owner=user).all())
            except IndexError:
                loc = self.create_location(Point(-74.1409, 40.5806), 'test1', user)
            item = ItemFactory.create(owner = user,
                                      name = fake_item['name'],
                                      description = fake_item['description'],
                                      categories = self.get_random_model_instance(ItemCategory),
                                      amount = random.randint(1, 1000),
                                      location = loc,
                                      deleted = False,
                                      status = random.randint(0,2),
                                      is_needed = fake_item['is_needed'])
            #item_type = 'need' if item.is_needed else 'have'
            print("Created " + item_type + ": " + item.name 
                + " with owner " + user.username + " and description: "
                + item.description + "...", end="\n")

        print("Success!")

    def load_json(self, path):
        print("Loading JSON...")
        json_data = open(path)
        data = json.load(json_data)
        json_data.close()
        return data
    
    def get_random_model_instance(self, model):
        total = model.objects.count()
        obj = None
        while obj == None:
            instance = random.randint(1, total)
            obj = get_object_or_None(model, pk=instance)
        return obj

    def create_location(self, point, name, user, default=False):
      print("Adding location " + name + " to " + user.username + "...", end="")
      location = get_object_or_None(Location, point=point, name=name, owner=user)
      if location:
        print("but already exists!", end="\n")
        return location
      else:
        location = LocationFactory.build(point=point,
                                         name=name,
                                         owner=user)
        location.clean()
        location.save()
        if default:
            user.get_profile().make_location_default(location)
        print("Success!", end="\n")
        return location
