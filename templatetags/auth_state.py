from django import template

register = template.Library()

@register.inclusion_tag('gallery/_auth_state.html', takes_context=True)
def auth_state(context):
    request = context['request']

    from django.contrib.auth.models import User
    from django.core.urlresolvers import reverse
    
    if request.user.is_active:
        return {'calltoaction': 'Logout', 'link': reverse('logout'), 'path': request.path}
    else:
        return {'calltoaction': 'Login', 'link': reverse('login'), 'path': request.path}
