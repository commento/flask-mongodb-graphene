""" app.py """
from flask import Flask
from flask_graphql import GraphQLView

from database import client
from schema import schema

from flask import Flask
from flask_restful import Api
from resources.person import Person

app = Flask(__name__)
api = Api(app)


@app.route("/health")
def healthcheck():
    return "Healthy Endpoint"


api.add_resource(Person, '/person')

app.debug = True


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


if __name__ == "__main__":
    app.run(port=5002)
