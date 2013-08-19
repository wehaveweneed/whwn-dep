import factory
import datetime
import random
from whwn.models import (Item, ItemCategory, ItemSKU,
                         Message, Team, UserProfile, WHWNUser)



class TeamFactory(factory.Factory):
    FACTORY_FOR = Team

    name = factory.Sequence(lambda n: "test-team-%s" % (n))
    description = ""

class UserProfileFactory(factory.Factory):
    FACTORY_FOR = UserProfile

    team = factory.SubFactory(TeamFactory)

class UserFactory(factory.Factory):
    FACTORY_FOR = WHWNUser

    username = factory.Sequence(lambda n: "test_user-%s" % (n))
    email = factory.Sequence(lambda n: "test-%s@example.com" % (n))
    userprofile = factory.RelatedFactory(UserProfileFactory, 'user')

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user 

class ItemCategoryFactory(factory.Factory):
    FACTORY_FOR = ItemCategory

    name = factory.Sequence(lambda n: 'test-category-%s' % (n))

class ItemSKUFactory(factory.Factory):
    FACTORY_FOR = ItemSKU
    
    upc = factory.Sequence(lambda n: 'test-upc-%s' % (n))
    team = factory.SubFactory(TeamFactory)
    name = factory.Sequence(lambda n: 'test-sku-item-%s' % (n))
    description = factory.Sequence(lambda n: 'test-description-%s')
    category = factory.SubFactory(ItemCategoryFactory)

class ItemFactory(factory.Factory):
    FACTORY_FOR = Item

    sku = factory.SubFactory(ItemSKUFactory)
    quantity = random.randint(1, 1000)
    requested = False
    possessor = None

class MessageFactory(factory.Factory):
    FACTORY_FOR = Message

    author = factory.SubFactory(UserFactory)
    contents = ""
    deleted = False
    flagged = False
    team = factory.SubFactory(TeamFactory)
