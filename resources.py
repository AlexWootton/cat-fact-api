import models
import collections

from flask import Blueprint, jsonify
from flask_restful import Resource, Api


class FactList(Resource):
    def get(self):
        # return all facts
        query = models.Fact.select()
        objects_list = []
        # loop over results and place into an ordered dict
        for i in query:
            d = collections.OrderedDict()
            d['_id'] = i._id
            d['text'] = i.text
            # append the ordered dicts to a list
            objects_list.append(d)
        # convert the list of dicts to a JSON response object and return it
        return jsonify(objects_list)


class Fact(Resource):
    def get(self, id):
        # return the fact that matches the provided id
        query = models.Fact.select().where(
            models.Fact._id == id
        )
        # place the results into a dict and convert to a JSON response
        return jsonify({'_id': query[0]._id, 'text': query[0].text})


# create the api blueprint for registration in main app file
facts_api = Blueprint('resources', __name__)
api = Api(facts_api)
# add endpoints to the api
api.add_resource(
    FactList,
    '/facts')
api.add_resource(
    Fact,
    '/facts/<id>')
