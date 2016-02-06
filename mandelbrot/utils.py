from collections import defaultdict
from django.db import models

import datetime
import json


class JSONEncoderPlus(json.JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, datetime.datetime):
            if obj.tzinfo is None:
                raise TypeError(
                    "date '%s' is not fully timezone qualified." % (obj))
            obj = obj.astimezone(pytz.UTC)
            return "{}".format(obj.isoformat())
        elif isinstance(obj, datetime.date):
            return "{}".format(obj.isoformat())
        return super(JSONEncoderPlus, self).default(obj, **kwargs)



def split(el):
    els = el.split(".", 1)
    if len(els) == 0:
        raise IndexError("What the hell did you give me")
    if len(els) == 1:
        return el, ""
    return els


def chunk(constraints):
    ret = defaultdict(list)
    for constraint in constraints:
        root, remainder = split(constraint)
        if remainder == "":
            remainder = constraint
            root = None  # "Top level" ID
        ret[root].append(remainder)
    return ret


def serialize(constraints, obj):
    ret = {}
    paths = chunk(constraints)

    if isinstance(obj, models.QuerySet):
        return [serialize(constraints, x) for x in obj]

    top_level = paths.pop(None, {})
    for key in top_level:
        # All the "None" keys are top level, and we'll just grab them
        # as we need them off the object.
        ret[key] = getattr(obj, key)

    for key, paths in paths.items():
        # So, in this case we've got a related object, and need to go ahead
        # and run over them, if we've got Many, otherwise, get the object,
        # and run with it.
        data = getattr(obj, key)
        if data is None:
            ret[key] = None
        elif isinstance(data, models.Model):
            ret[key] = serialize(paths, data)
        else:
            ret[key] = [serialize(paths, x) for x in getattr(obj, key).all()]

    return ret
