from django.contrib import admin
from django.urls import path, include
from .views import index, indexdb, TestImagesList, TestImageGet,TestDomain
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("indexdb", indexdb, name="index"),
    path('api-auth/', include('rest_framework.urls')),
    # DRF SPECTACULAR
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    ###
    path("list_test_images/", TestImagesList.as_view(), name="test-image-list"),
    path("get_test_image/<int:pk>/", TestImageGet.as_view(), name="test-image-get"),
    
    path("test_domain/", TestDomain.as_view(), name="test-domain")
    ]

if settings.DEBUG is True:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
