from django import template
from ..models import Menu

register = template.Library()

@register.inclusion_tag('menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    current_path = context['request'].path
    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.items.all()
    return {'menu_items': menu_items, 'current_path': current_path}