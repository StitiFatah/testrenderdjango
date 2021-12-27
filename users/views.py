from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken, SlidingToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


class BlacklistTokenView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as error:
            print(error)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class IsBlacklisted(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token_ = get_object_or_404(OutstandingToken, token=refresh_token)

            if BlacklistedToken.objects.filter(token=token_).exists():
                bl = "blacklisted"
            else:
                bl = "not blacklisted"

            return Response(bl, status=status.HTTP_200_OK)

        except Exception as error:

            return Response("error", status=status.HTTP_200_OK)


# class IsBlacklisted(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]

#             if not PreOutstandingToken.objects.get(token=refresh_token).exists():
#                 print("not in preoustanding")
#                 return Response(False)
#             else:
#                 try:
#                     outsanting_token = OutstandingToken.objects.get(
#                         token=refresh_token)
#                     if BlacklistedToken.objects.filter(token=refresh_token).exists():
#                         print("Token is Blacklisted")
#                         return(False)
#                     else:
#                         print("Token exist and is not Blacklisted)
#                         return(True)

#                 except OutstandingToken.DoesNotExist:
#                     print("outstanding token doesn't exist")
#                     return Response(False)
