from haystack import indexes

from whwn.models import Item

class ItemIndex(indexes.ModelSearchIndex, indexes.Indexable):

    class Meta:
        model = Item
