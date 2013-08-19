from django.db import models

class ItemCategory(models.Model):
    """
    Categories that items can reside in.

    Examples:
    Miscellaneous, Medicine, Bedding, Field Supplies, etc.
    """
    name = models.CharField(max_length=32)

    class Meta:
        app_label = "whwn"

    def __unicode__(self):
        return self.name

    def items(self):
        """:returns: Queryset of Items in this category."""
        raise NotImplementedError
