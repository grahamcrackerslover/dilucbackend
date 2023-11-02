from django.contrib import admin
from .models import Item, Purchase

def copy_items(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Clear the primary key to create a new object
        obj.save()

copy_items.short_description = 'Copy selected items'

class ItemAdmin(admin.ModelAdmin):
    actions = [copy_items]

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Purchase)
