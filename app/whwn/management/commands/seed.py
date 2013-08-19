from __future__ import print_function
from django.core.management.base import NoArgsCommand, CommandError
from django.core.management import call_command
import random
import datetime
from faker import Faker
from annoying.functions import get_object_or_None
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from django.contrib.gis.geos import Point
from whwn.models import (Item, ItemCategory, ItemSKU, Message, Team, User)
from whwn.factories import (UserFactory, ItemSKUFactory, ItemFactory, 
                       UserProfileFactory, MessageFactory, TeamFactory)

import json
from pprint import pprint


class Command(NoArgsCommand):
    help = 'Seeds the database with data defined in the seed.py file'

    f = Faker()

    def get_random_model_instance(self, model):
      return model.objects.order_by('?')[0]

    def get_random_model_instance_except(self, model, inst):
      obj = None;
      while obj is None:
        tmp = self.get_random_model_instance(model)
        if tmp != inst:
          obj = tmp
      return obj

    def handle_noargs(self, **options):
        
        print("Flushing database data to prepare for seed... ", end="\n")
        Item.objects.all().delete()
        ItemSKU.objects.all().delete()
        ItemCategory.objects.all().delete()
        Message.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        print("Creating teams... ", end="\n")
        # START TEAM CREATION #
        whwn = TeamFactory.create(
            name="We Have We Need",
            description=("We are the world, we are the children. "
                           "We are the ones who make a brighter day "
                           "So lets start giving."),
            primary_user=None
        )
        # END TEAM CREATION #

        print("Creating users... ", end="\n")
        # START USER CREATION #
        lewis = UserFactory.create(
            username = "lewisf",
            first_name = "Lewis",
            last_name = "Chung",
            email = "lewis.f.chung@gmail.com",
            password = "foobar1",
            userprofile__team = whwn,
        )
        jon = UserFactory.create(
            username = "jnwng",
            first_name = "Jon",
            last_name = "Wong",
            email = "j@jnwng.com",
            password = "foobar1",
            userprofile__team = whwn,
        )
        wes = UserFactory.create(
            username = "wesvetter",
            first_name = "Wes",
            last_name = "Vetter",
            email = "wes.vetter@gmail.com",
            password = "foobar1",
            userprofile__team = whwn,
        )
        zack = UserFactory.create(
            username = "zgrannan",
            first_name = "Zack",
            last_name = "Grannan",
            email = "zgrannan@gmail.com",
            password = "foobar1",
            userprofile__team = whwn,
        )

        jenner = UserFactory.create (
            username = "jenner",
            first_name = "Jenner",
            last_name = "LaFave",
            email = "jenner@jfave.com",
            password = "bestpony",
            userprofile__team = whwn,
        )
        # END USER CREATION #

        print("Creating item categories... ", end="\n")
        # START ITEM CATEGORY CREATION #
        from django.core.management import call_command
        call_command("loaddata", "initial_data.json", verbosity=0)
        misc, medicine, bedding = ItemCategory.objects.all()[:3]
        # END ITEM CATEGORY CREATION #

        print("Creating items... ", end="\n")
        # START ITEMSKU, ITEM CREATION #
        # Depending on how we handle ItemSKU creations later, we might #
        # want to change this #

        sku1 = ItemSKUFactory.create(team = whwn, name = "Bottled Water", category = misc)
        sku2 = ItemSKUFactory.create(team = whwn, name = "Tetracycline Pills", category = medicine)
        sku3 = ItemSKUFactory.create(team = whwn, name = "Blankets", category = bedding)
        sku4 = ItemSKUFactory.create(team = whwn, name = "Bandages", category = medicine)
        sku5 = ItemSKUFactory.create(team = whwn, name = "Beef Jerky", category = misc)
        sku6 = ItemSKUFactory.create(team = whwn, name = "Neosporin", category = medicine)
        sku7 = ItemSKUFactory.create(team = whwn, name = "Gauze Pads", category = misc)
        sku8 = ItemSKUFactory.create(team = whwn, name = "Duct Tape", category = misc)
        ItemFactory.create(sku = sku1, quantity = 400, requested=True, possessor=wes)
        ItemFactory.create(sku = sku2, quantity = 123, requested=True, possessor=lewis)
        ItemFactory.create(sku = sku3, quantity = 230, requested=True, possessor=zack)
        ItemFactory.create(sku = sku4, quantity = 1, requested=True, possessor=jon)
        ItemFactory.create(sku = sku5, quantity = 15, requested=True, possessor=wes)
        ItemFactory.create(sku = sku6, quantity = 40, requested=False, possessor=zack)
        ItemFactory.create(sku = sku7, quantity = 512, requested=False)
        ItemFactory.create(sku = sku8, quantity = 850, requested=False, possessor=jon)

        # END ITEMSKU, ITEM CREATION #

        print("Creating messages... ", end="\n")
        # START MESSAGE CREATION #
        for x in range(50):
            MessageFactory.create(
                author = self.get_random_model_instance(User),
                contents = self.f.lorem()[0: random.randint(10,50)],
                team = whwn,
            )
        # END MESSAGE CREATION #


