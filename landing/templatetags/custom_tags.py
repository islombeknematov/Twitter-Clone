from django import template
from social.models import NotificationModel

register = template.Library()


@register.inclusion_tag('show_notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = NotificationModel.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-created_at')
    return {'notifications': notifications}


