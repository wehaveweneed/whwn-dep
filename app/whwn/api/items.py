from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.serializers import Serializer

from whwn.models import Item, ItemCategory, ItemSKU
from whwn.api.users import UserResource


class ItemSKUAuthorization(Authorization):
    def is_authorized(self, object_list, bundle):
        return object_list.filter(team=bundle.request.user.get_profile().team)

class ItemSKUResource(ModelResource):
    class Meta:
        queryset = ItemSKU.objects.all()
        resource_name = "ItemSKU"
        allowed_methods = ['get']
        authorization = ItemSKUAuthorization()

        fields = ["upc", "team", "name", "description", "category"]

class ItemCategoryResource(ModelResource):
    class Meta:
        queryset = ItemCategory.objects.all()
        resource_name = "ItemCategory"
        allowed_methods = ["get"]
        fields = ["name", "id"]


class ItemAuthorization(Authorization):
    def is_authorized(self, object_list, bundle):
        team = bundle.request.user.get_profile().team
        return object_list.filter(sku__team=team)


class ItemResource(ModelResource):
    possessor = fields.ToOneField(UserResource, 'possessor', null=True)
    sku = fields.ToOneField(ItemSKUResource, 'sku')
    name = fields.CharField(attribute='name')
    category = fields.ToOneField(ItemCategoryResource, 'category')

    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'

        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        excludes = ['created_at', 'updated_at']
        authentication = ApiKeyAuthentication()
        authorization = ItemAuthorization()
        serializer = Serializer(formats=['json'])
        filtering = {
            'requested': 'exact'
        }
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        """ This method creates an itemSKU for an item if not SKU is provided
        """
        category = None
        id = bundle.data.get("id")
        if not bundle.data.get("name"):
            raise ValueError("Item name is required")
        if not bundle.data.get("category"):
            category = ItemCategory.objects.get(name="Other Supplies")
        else:
            category =\
            ItemCategoryResource().get_via_uri(bundle.data["category"])

        # set possessor
        if bundle.data.get("possessor", None):
            possessor = UserResource().get_via_uri(bundle.data["possessor"])
        else:
            possessor = None

        team = bundle.request.user.get_profile().team
        sku = ItemSKU.objects.get_or_create(team=team, name=bundle.data["name"],
                category=category)
        quantity = int(bundle.data["quantity"]) if "quantity" in bundle.data else 1
        if id:
            Item.objects.filter(id=id).update(sku=sku[0], quantity=quantity, possessor=possessor)
            bundle.obj = Item.objects.get(id=id)
        else:
            bundle.obj = Item.objects.create(sku=sku[0], quantity=quantity)
        return bundle
