from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def categories(request):
    categories = Category.objects.all()

    return Response(
        {
            "success": True,
            "categories": categories,
        },
    )
