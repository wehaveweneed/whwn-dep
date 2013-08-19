from django.contrib.auth.models import User
from django.db import transaction
from annoying.functions import get_object_or_None
from whwn.utils import ensure_positive, ensure_greater_equal_than
from whwn.models import Item

class WHWNUser(User):
    """
    WHWNUser are django contrib.auth.model.User models with added
    custom functions used specifically within the WHWN application.

    NOTE: This may cause problems, as some functions may expect a
    django User object. For this reason, there is a provided
    to_django_user().
    """

    class Meta:
        proxy = True

    @transaction.commit_on_success()
    def checkout(self, item, quantity=None):
        """
        Checkout an item.

        :param item: item to checkout
        :type item: whwn.models.Item
        :param quantity: quantity of the item to checkout, defaults to all.
        :type quantity: int
        :returns: checked out item
        :rtype: whwn.models.Item
        """

        if quantity is None: 
            quantity = item.quantity

        ensure_positive(quantity)
        ensure_greater_equal_than(item.quantity, quantity)

        item.quantity -= quantity
        item.save()
        return Item.objects.create(possessor=self, quantity=quantity, sku=item.sku)


    @transaction.commit_on_success()
    def checkin(self, item, quantity=None):
        """
        Checkin an item.

        :param item: item to checkin
        :type item: whwn.models.Item
        :param quantity: quantity of the item to checkin, defaults to all.
        :type quantity: int
        :returns: item that recieved the amount from checkin
        :rtype: whwn.models.Item
        """
        if quantity is None:
            quantity = item.quantity

        ensure_positive(quantity)
        ensure_greater_equal_than(item.quantity, quantity)

        existing_item = get_object_or_None(Item, sku=item.sku, possessor=None)

        item.consume(quantity)
        item.save()
        if existing_item:
            print existing_item.quantity
            existing_item.refill(quantity)
            print existing_item.quantity
            existing_item.save()
        else:
            return Item.objects.create(sku=item.sku, quantity=quantity, possessor=None)

    def join_team(self, team):
        """
        Sets the user's team.

        :param team:
        :type whwn.models.Team:
        :returns: the Team if successful, else None
        :rtype: whwn.models.Team
        """
        profile = self.get_profile()
        profile.team = team;
        profile.save()
        return profile.team

    def items(self):
        return self.item_set.all()

    def items_have(self):
        return Item.objects.filter(requester=self, requested=False)

    def items_need(self):
        return Item.objects.filter(requester=self, requested=True)

    def to_django_user(self):
        """
        Returns the django.contrib.auth.models.User version of this
        WHWNUser. Used in cases where a User type is expected.

        :returns: django user
        :rtype: django.contrib.auth.models.User
        """
        user = User()
        user.__dict__ = self.__dict__
        return user

