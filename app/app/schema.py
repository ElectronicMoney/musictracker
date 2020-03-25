from graphene_django import DjangoObjectType
import graphene
import Tracks.schema


class Query(Tracks.schema.Query, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query)