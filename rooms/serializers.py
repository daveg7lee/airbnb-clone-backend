from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from .models import Amenity, Room


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):

    rating = SerializerMethodField()
    is_owner = SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
        )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    category = CategorySerializer(
        read_only=True,
    )
    rating = SerializerMethodField()
    is_owner = SerializerMethodField()

    class Meta:
        model = Room
        exclude = ("amenities",)

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user
