from django import template

register = template.Library()


@register.filter(name='human_list')
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
