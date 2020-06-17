import collections
import json


def ConvertToPretty(query):
    """Returns a formatted string"""
    output = ''
    for i in query:
        output += 'ID: {} | {}\n'.format(i._id, i.text)
    return output


def ConvertToJson(query):
    """Returns a serialised JSON string"""
    objects_list = []
    for i in query:
        d = collections.OrderedDict()
        d['_id'] = i._id
        d['text'] = i.text
        objects_list.append(d)
    return json.dumps(objects_list)
