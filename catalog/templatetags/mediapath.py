from django import template
from django.conf import settings
from django.templatetags.static import PrefixNode

register = template.Library()


@register.simple_tag
def mediapath(path):
    return PrefixNode.handle_simple("MEDIA_URL" + path)
