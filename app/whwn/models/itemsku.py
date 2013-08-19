from django.db import models
from whwn.models.abstract import Timestamps

class ItemSKU(Timestamps):
    """
    ItemSKU's operate to keep track of item meta data. They are
    unique per item per team, so for example, all "Box of 50, Tylenol
    Extra Strength" on a single team will share an ItemSKU.

    ItemSKU's include a UPC, which is guaranteed to be unique. The intent
    for this is to use standard product UPC's to prevent duplicate entries
    of the same product on a team inventory.
    """
    upc = models.CharField(null=True, blank=True, max_length=64)
    team = models.ForeignKey("whwn.Team")
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey("whwn.ItemCategory")

    class Meta:
        app_label = "whwn"
        unique_together = ('upc', 'team')
