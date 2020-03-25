from graphene_django import DjangoObjectType
import graphene
from .models import Track
from Users.schema import UserType

class TrackType(DjangoObjectType):
    class Meta:
        model = Track

# Get Track
class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()

# Create Track
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

# Update Track
class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        url  = graphene.String()

    def mutate(self, info, **kwargs):
        # Get the track using track_id
        track = Track.objects.get(id = kwargs.get('track_id'))
        # If user from context is ot equal to posted_by
        if info.context.user != track.posted_by:
            raise Exception('Not permited to update this track!')

        title       = kwargs.get('title')
        description = kwargs.get('description')
        url         = kwargs.get('url')
        # Save track
        track.save()
        # return the created track
        return UpdateTrack(track=track)


# Delete Track
class DeleteTrack(graphene.Mutation):
    track_id = graphene.Int()

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        # Get the track using track_id
        track = Track.objects.get(id = kwargs.get('track_id'))
        # If user from context is ot equal to posted_by
        if info.context.user != track.posted_by:
            raise Exception('Not permited to delete this track!')

        # Save track
        track.delete()
        # return the created track
        return DeleteTrack(track_id=track_id)


# Create Track
class CreateLike(graphene.Mutation):
    user = graphene.Field(UserType)
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        track_id = graphene.Int(required=True)
        user = info.context.user

        if user.is_anonymous:
            raise Exception('You must Login to Like Tracks!')
        # Create Track
        track = Track.objects.get(id=kwargs.get('track_id'))
        # Check if not track with such id
        if not track:
            raise Exception("Cannot find any track with given id!")

        track.save()
        # return the created track
        return CreateLike(user=user, track=track)

class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()
    create_like  = CreateLike.Field()

schema = graphene.Schema(query=Query)