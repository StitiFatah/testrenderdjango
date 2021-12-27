from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import BlacklistTokenView, IsBlacklisted


app_name = "users"

urlpatterns = [
    # Logout + Blacklist Token
    path('api/blacklist_logout/',
         BlacklistTokenView.as_view(), name='logout_blacklist'),
    path("token_is_blacklisted/", IsBlacklisted.as_view(), name="is-blacklisted")

]
