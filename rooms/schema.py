import strawberry
import typing
from . import types
from . import quries
from . import mutations
from common.permissions import OnlyLoggedIn


@strawberry.type
class Query:
    all_rooms: typing.List[types.RoomType] = strawberry.field(resolver=quries.get_all_rooms)
    room: typing.Optional[types.RoomType] = strawberry.field(resolver=quries.get_room)


@strawberry.type
class Mutation:
    room: typing.Optional[types.RoomType] = strawberry.mutation(
        resolver=mutations.add_room, permission_classes=[OnlyLoggedIn]
    )
