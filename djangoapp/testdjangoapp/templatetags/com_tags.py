from django import template
from testdjangoapp.models import CMenu
register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = CMenu.objects.all()
    return {
        "menu_items": menu_items,
    }
