from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def categories(request):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            return Response({"created": True})
        else:
            return Response(serializer.errors)


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)

    return Response(serializer.data)
