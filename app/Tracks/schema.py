from graphene_django import DjangoObjectType
import graphene
from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track

class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()

class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url  = graphene.String()

    def mutate(self, info, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        url = kwargs.get('url')

        user = info.context.user
        if user.is_anonymous:
            raise Exception('You are not Logged In!')
        return user

        # Create Track
        track = Track(title=title, description=description, url=url, posted_by=user)
        track.save()
        # return the created track
        return CreateTrack(track=track)

class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()

schema = graphene.Schema(query=Query)