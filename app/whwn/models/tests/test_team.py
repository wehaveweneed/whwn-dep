from django.test import TestCase

from whwn.models import WHWNUser
from whwn.factories import (TeamFactory, ItemSKUFactory, UserFactory,
                            UserProfileFactory, ItemFactory)

class TeamTestCase(TestCase):

    def setUp(self):
        self.team = TeamFactory.create()
        self.sku = ItemSKUFactory.create(team=self.team)
        self.user1 = UserFactory.create(userprofile__team=self.team)
        self.user2 = UserFactory.create(userprofile__team=self.team)
        self.item1 = ItemFactory.create(sku=self.sku, quantity=5)
        self.item2 = ItemFactory.create(sku=self.sku, quantity=4, possessor=self.user1)

    def test_get_items(self):
        self.assertEquals(len(self.team.items()), 2)
        items = self.team.items()
        self.assertTrue(self.item1 in items and self.item2 in items) 

    def test_get_members(self):
        members = self.team.members()
        self.assertTrue(self.user1 in members and self.user2 in members)

    def test_first_member_set_as_primary_user(self):
        teamX = TeamFactory.create()
        userX = UserFactory.create(userprofile__team=teamX)
        self.assertEquals(WHWNUser.objects.get(id=teamX.primary_user.id), userX)
