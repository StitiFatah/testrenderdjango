from django.http import HttpRequest, HttpResponse
from users.models import PersoUser
from .models import TestImages
from .serializers import TestImagesSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions


def index(request):
    admin = PersoUser.objects.get(is_admin=True)
    return HttpResponse(f"Hello guys my name is {admin.username}")


class TestImagesList(ListAPIView):
    serializer_class = TestImagesSerializer
    queryset = TestImages.objects.all()


class TestImageGet(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TestImagesSerializer
    queryset = TestImages.objects.all()
