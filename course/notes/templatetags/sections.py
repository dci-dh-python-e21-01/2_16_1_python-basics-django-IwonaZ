from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def linked_section(section_name):
    section_name.replace(" ", "")
    link = [
        '<a href="',
        reverse("notes:section_details", args=[section_name]),
        '">',
        section_name,
        "</a>",
    ]
    return "".join(link)


@register.filter
def remove_spaces(section_name):
    return section_name.replace(" ", "%20")
