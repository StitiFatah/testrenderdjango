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

        # resp = {
        # "http_host": request.META["HTTP_HOST"],
        # "http_origin": request.META["HTTP_ORIGIN"],
        # }

        # resp = {
        # "meta": str(request.META)
        # }

        resp = request.headers

        return Response(resp, status=status.HTTP_200_OK)


def get_header(http_headers_dict, header_name):
    try:
        return http_headers_dict[header_name]
    except KeyError:
        return False


def no_test_get_domain_name_from_request(request):

    http_headers_dict = request.headers
    print(http_headers_dict)

    header_names = ["Referer", "Origin"]

    for name in header_names:
        domain = get_header(http_headers_dict=http_headers_dict, header_name=name)
        if domain:
            return domain

    raise Exception("Cannot find domain from HTTP headers' from request")


class GetHeaders(APIView):
    def get(self, request, *args, **kwargs):

        # domain = no_test_get_domain_name_from_request(request=request)
        headers = request.headers

        print(headers)

        return Response(headers)
