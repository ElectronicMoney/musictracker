from graphene_django import DjangoObjectType
import graphene
import Tracks.schema
import Users.schema

# Queries
class Query(
    Tracks.schema.Query, 
    graphene.ObjectType
):
   pass

# Mutations
class Mutation(
    Users.schema.Mutation, 
    Tracks.schema.Mutation, 
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)