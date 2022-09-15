from django import template
from owner.models import Owner, OwnerExpertAt
register = template.Library()


@register.simple_tag(name='services')
def function(side):
    owner = Owner.objects.all()[0]
    expert_at = OwnerExpertAt.objects.filter(owner=owner)
    number_of_item = expert_at.count()
    if side == 'left':
        expert_at = expert_at[:int(number_of_item/2)]
    elif side == 'right':
        expert_at = expert_at[int(number_of_item / 2):]

    return {'expert_at': expert_at}
