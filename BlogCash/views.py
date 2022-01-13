from django.http import HttpRequest, HttpResponse
from users.models import PersoUser
from .models import TestImages
from .serializers import TestImagesSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Hello guys")


def indexdb(request):
    admin = PersoUser.objects.get(is_admin=True)
    return HttpResponse(f"Hello guys my name is {admin.username}")


class TestImagesList(ListAPIView):
    serializer_class = TestImagesSerializer
    queryset = TestImages.objects.all()


class TestImageGet(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TestImagesSerializer
    queryset = TestImages.objects.all()

class TestDomain(APIView):

    def get(self, request, *args, **kwargs):

        # resp = str(request.META)
        # resp = "hello"

        resp = {
            "http_host": request.META["HTTP_HOST"],
            "http_origin": request.META["HTTP_ORIGIN"],
        }

        resp = {
            "meta": str(request.META)
        }

        return Response(resp, status=status.HTTP_200_OK)


