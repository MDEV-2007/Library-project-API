
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from dj_rest_auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetConfirmView,PasswordResetView,UserDetailsView


schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/",
        contact=openapi.Contact(email="uzbekcoders0706@gmail.com",),
        license=openapi.License(name="MDEV License"),
    ),
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None),),
]

