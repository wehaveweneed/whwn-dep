from django.test import TestCase

from whwn.models import Item, ItemCategory
from whwn.factories import (ItemFactory, UserFactory, TeamFactory,
                            ItemCategoryFactory, ItemSKUFactory,
                            UserFactory, UserProfileFactory)

class ItemTestCase(TestCase):


    def setUp(self):
        self.team = TeamFactory.create()
        self.user1 = UserFactory.create(userprofile__team=self.team)
        self.user2 = UserFactory.create(userprofile__team=self.team)
        self.sku = ItemSKUFactory.create(team=self.team)
        self.item = ItemFactory.create(sku=self.sku, quantity=5)

    def test_consume(self):
        self.item.consume(2)
        self.assertEquals(self.item.quantity, 3) 

        # Should not be able to consume more items that are available
        try:
            self.item.consume(10)
            self.fail()
        except:
            pass

        # Should not be able to consume a negative amount of items
        try:
            self.item.consume(-3)
            self.fail()
        except:
            pass

    def test_refill(self):
        self.item.refill(2)
        self.assertEquals(self.item.quantity, 7)

        # Should not be able to refill in a negative amount of items
        try:
            self.item.refill(-3)
            self.fail()
        except:
            pass

    def test_zero_quantity_delete(self):
        self.item.consume(5)
        self.assertEquals(self.item, None)
