""" schema.py """
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Game as GameModel
from models import Powerup as PowerupModel
from models import Enemy as EnemyModel
from models import Level as LevelModel
from models import Person as PersonModel


class Game(MongoengineObjectType):
    class Meta:
        description = "Game"
        model = GameModel
        interfaces = (Node,)


class Powerup(MongoengineObjectType):
    class Meta:
        description = "Power-ups"
        model = PowerupModel
        interfaces = (Node,)


class Enemy(MongoengineObjectType):
    class Meta:
        description = "Enemies"
        model = EnemyModel
        interfaces = (Node,)


class Level(MongoengineObjectType):
    class Meta:
        description = "Levels"
        model = LevelModel
        interfaces = (Node,)


class Person(MongoengineObjectType):
    class Meta:
        description = "Person"
        model = PersonModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()

    all_levels = MongoengineConnectionField(Level)
    all_enemies = MongoengineConnectionField(Enemy)
    all_powerups = MongoengineConnectionField(Powerup)
    all_games = MongoengineConnectionField(Game)
    all_persons = MongoengineConnectionField(Person)


schema = graphene.Schema(query=Query, types=[Powerup, Level, Enemy, Game, Person])
