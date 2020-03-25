from graphene_django import DjangoObjectType
import graphene
import graphql_jwt

import Tracks.schema
import Users.schema

# Queries
class Query(
    Users.schema.Query, 
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
    # Add django-graphql-jwt mutations to the root schema:
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)