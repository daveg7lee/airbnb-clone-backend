import strawberry
import typing
from . import types
from . import quries
from common.permissions import OnlyLoggedIn


@strawberry.type
class Query:
    all_rooms: typing.List[types.RoomType] = strawberry.field(
        resolver=quries.get_all_rooms, permission_classes=[OnlyLoggedIn]
    )
    room: typing.Optional[types.RoomType] = strawberry.field(resolver=quries.get_room)
