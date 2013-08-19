from django.test import TestCase

from whwn.factories import (TeamFactory, ItemSKUFactory, UserFactory,
                            ItemFactory)

from whwn.models import Item

class UserTestCase(TestCase):

    def setUp(self):
        self.team = TeamFactory.create()
        self.user1 = UserFactory.create(userprofile__team=self.team)
        self.user2 = UserFactory.create(userprofile__team=self.team)
        self.sku = ItemSKUFactory.create(team=self.team)
        self.item = ItemFactory.create(sku=self.sku, possessor=self.user1, quantity=5)

    def test_checkout(self):
        item2 = self.user2.checkout(self.item, 3)
        self.assertEquals(len(self.user2.items()), 1)
        self.assertEquals(len(self.user1.items()), 1)
        self.assertEquals(self.user2.items()[0].quantity, 3)
        self.assertEquals(self.user1.items()[0].quantity, 2)
        self.assertEquals(self.user2.items()[0].sku, self.user1.items()[0].sku)

    def test_checkout_over_quantity(self):
        try:
            self.user2.checkout(self.item, 6)
            self.fail()
        except:
            pass

    def test_checkin(self):
        self.user1.checkin(self.item, 3)
        self.assertEquals(self.item.quantity, 2)
        items = Item.objects.filter(sku=self.sku)
        self.assertEquals(len(items), 2)

    def test_checkin_with_existing_team_pool(self):
        # a pool is defined in this case as an item with no possessor
        item2 = ItemFactory.create(sku=self.sku, possessor=None, quantity=5)
        self.user1.checkin(self.item, 3)
        self.assertEquals(item2.quantity, 8)
        self.assertEquals(self.item.quantity, 2)
