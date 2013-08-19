from django.test import TestCase

from whwn.models import Item, ItemCategory
from whwn.factories import (ItemFactory, UserFactory, TeamFactory,
                            ItemCategoryFactory, ItemSKUFactory,
                            UserFactory, UserProfileFactory)

class ItemTestCase(TestCase):


    def setUp(self):
        self.team = TeamFactory.create()
        self.category = ItemCategoryFactory.create()
        self.sku1 = ItemSKUFactory.create(team=self.team)
        self.sku2 = ItemSKUFactory.create(team=self.team)
        self.item1 = ItemFactory.create(sku=self.sku1, quantity=5)
        self.item2 = ItemFactory.create(sku=self.sku1, quantity=9)
        self.item3 = ItemFactory.create(sku=self.sku2, quantity=1)
        self.item4 = ItemFactory.create(sku=self.sku2, quantity=4)

    def test_item_set(self):
        items = self.category.items()
        assertTrue(self.item1 in items)
        assertTrue(self.item2 in items)
        assertTrue(self.item3 in items)
        assertTrue(self.item4 in items)
