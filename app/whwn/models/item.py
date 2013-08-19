from whwn.models import ItemSKU
from whwn.models.abstract import Timestamps, Locatable
from django.contrib.auth.models import User
from django.db import models
from whwn.utils import ensure_positive, ensure_greater_equal_than


class Item(Timestamps, Locatable):
    """
    Item model represents an item. Every item has an Item stock keeping unit
    represented in the relationship to the SKU model that contains information
    about the item itself, whereas the Item model is only concerned with an item
    in an inventory with an attached quantity.
    """

    sku = models.ForeignKey(ItemSKU)
    quantity = models.PositiveIntegerField()
    requested = models.BooleanField(default=False)
    possessor = models.ForeignKey(User, null = True, blank = True)

    def _get_name(self):
        return self.sku.name

    def _get_category(self):
        return self.sku.category

    name = property(_get_name)
    category = property(_get_category)

    class Meta:
        app_label = "whwn"

    def consume(self, quantity):
        """
        :param quantity: quantity of an item that is consumed
        """
        ensure_positive(quantity)
        ensure_greater_equal_than(self.quantity, quantity)
        
        self.quantity -= quantity
        self.save()

    def refill(self, quantity):
        """
        :param quantity: quantity that is added
        """
        ensure_positive(quantity)

        self.quantity += quantity
        self.save()

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.delete()
        else:
            return super(Item, self).save(*args, **kwargs)
