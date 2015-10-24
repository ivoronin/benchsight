from django import template
from django.utils.http import urlencode

register = template.Library()

@register.assignment_tag(takes_context=True)
def qscut(context, cut):
    items = context['request'].GET.items()
    return urlencode({k:v for k,v in items if k!=cut})
