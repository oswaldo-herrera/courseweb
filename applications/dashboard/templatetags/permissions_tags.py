import re
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='tiene_permiso')
def tiene_permiso(user, permiso):
    return user.has_perm(permiso)


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False
    



@register.filter
def regex_search(value, pattern):
    match = re.search(pattern, value)
    if match:
        return match.group(1)
    return value