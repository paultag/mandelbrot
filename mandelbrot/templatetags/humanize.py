from django import template

import datetime as dt
import humanize
import humanize.time

register = template.Library()


@register.filter(name='humanize_delta')
def humanize_delta(value):
    return humanize.naturaltime(
        dt.datetime.now(dt.timezone.utc) - value)


@register.filter(name='humanize_timedelta')
def humanize_delta(value):
    return humanize.time.naturaldelta(value)


@register.filter(name='humanize_date')
def humanize_delta(value):
    return dt.datetime.strftime(value, "%a, %b %d, %Y, %I:%M %p %Z")


@register.filter(name='humanize_list')
def human_list(values):
    names = [x.name for x in values]

    if len(names) == 0:
        return ""
    if len(names) == 1:
        return names[0]

    entities = names[:-1]
    last = names[-1]
    return "{} & {}".format(
        ", ".join(entities),
        last,
    )
