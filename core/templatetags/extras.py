from django import template

register = template.Library()

@register.filter(name='get_val')

def get_vat(dict, key):
    return dict.get(key)

@register.filter
def dict_unique(queryset, field):
    return queryset.values(field).distinct()