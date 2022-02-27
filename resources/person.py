from flask_restful import Resource, reqparse
import logging
from pymongo import MongoClient
from mongoengine import connect

import json
from bson import ObjectId

from models import Person as PersonMongo


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


DATABASE = "flask-mongodb-graphene"


parser = reqparse.RequestParser()
parser.add_argument('first_name', type=str, required=True)
parser.add_argument('last_name', type=str, required=True)
parser.add_argument('age', type=int, required=False)


class Person(Resource):

    def get(self):
        return "ciao", 200

    def post(self):
        req_args = parser.parse_args()
        # client = connect(
        #     DATABASE,
        #     host=f"mongodb://localhost:27017",
        #     alias="default",
        # )
        # person = PersonMongo(first_name=req_args['first_name'],
        #                      last_name=req_args['last_name'],
        #                      age=req_args.get('age')
        #                 )
        # person.save()
        doc = {
            'first_name': req_args['first_name'],
            'last_name': req_args['last_name'],
            'age': req_args.get('age')
        }
        c = MongoClient('localhost', 27017)
        db = c[DATABASE]
        _id = db['person'].insert_one(doc).inserted_id
        doc["id"] = JSONEncoder().encode(_id)
        del doc["_id"]
        return doc, 201
        # return person.to_json(), 201
