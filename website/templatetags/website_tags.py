from django import template
from website.models import WebsiteSpecification, KeyWord

register = template.Library()


@register.simple_tag(name='keywords')
def function():
    keywords = KeyWord.objects.all()
    keywords_list = []
    for k in keywords:
        keywords_list.append(k.keyword)
    return ", ".join(keywords_list)


@register.simple_tag(name='meta_author')
def function():
    website_sp = WebsiteSpecification.objects.all()[0]
    return str(website_sp.meta_author)


@register.simple_tag(name='meta_title')
def function():
    website_sp = WebsiteSpecification.objects.all()[0]
    return str(website_sp.meta_title)


@register.simple_tag(name='meta_description')
def function():
    website_sp = WebsiteSpecification.objects.all()[0]
    return str(website_sp.meta_description)


