from django import template
from experiments.utilts import get_user_experiments


register = template.Library()


@register.simple_tag()
def user_experiments(request):
    return get_user_experiments(request)
