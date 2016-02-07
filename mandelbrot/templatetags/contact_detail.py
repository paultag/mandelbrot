from django import template

import datetime as dt
import humanize
import humanize.time

register = template.Library()


@register.filter(name='contact_detail_fontawesome')
def contact_detail_fontawesome(cd):
    return {
        "phone": "fa-mobile",
        "email": "fa-envelope-o",
        "fax": "fa-fax",
        "github": "fa-github-alt",
        "twitter": "fa-twitter",
        "yo": "fa-square",
        "website": "fa-external-link",
        "slack": "fa-slack",
    }.get(cd.type, 'fa-link')


@register.filter(name='contact_detail_href')
def contact_detail_href(cd):
    return {
        "phone": "tel:{}",
        "email": "mailto:{}",
        "fax": "fax:{}",
        "github": "https://github.com/{}",
        "twitter": "https://twitter.com/@{}",
        "yo": "yo:{}",
        "slack": "https://veteranaffairs.slack.com/messages/{}/",
    }.get(cd.type, '{}').format(cd.value)
