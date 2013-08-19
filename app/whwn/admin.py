from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.db import models
from django.views.generic import TemplateView

from whwn.models import ItemCategory, Item, UserProfile, Message

from adminplus import AdminSitePlus

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'possessor')

    def queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_select_related = True
    inlines = [UserProfileInline]

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_select_related = True
    inlines = [UserProfileInline]

admin.site = AdminSitePlus()
admin.site.register(Message, ModelAdmin)
admin.site.register(ItemCategory, ModelAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(User, UserAdmin)

class FaqAdminView(TemplateView):
    template_name = "admin/question_input.html"

    def get_context_data(self, **kwargs):
        return {}

admin.site.register_view("faq", FaqAdminView.as_view())
