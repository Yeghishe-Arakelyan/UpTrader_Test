from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Menu, MenuItem

class MenuItemAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'url', 'menu')
    list_display_links = ('indented_title',)

admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)