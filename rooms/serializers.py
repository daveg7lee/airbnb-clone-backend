from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from wishlists.models import Wishlist
from .models import Amenity, Room
from medias.serializers import PhotoSerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "pk",
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):

    rating = SerializerMethodField()
    is_owner = SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

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
            "photos",
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
    is_liked = SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        exclude = ("amenities",)

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    def get_is_liked(self, room):
        request = self.context["request"]
        if request.user.is_authenticated:
            return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()
        return False
