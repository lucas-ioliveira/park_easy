"""
URL configuration for park_easy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Park Easy API",
        default_version="v1",
        description="API documentation for Park Easy",
        contact=openapi.Contact(email="lucasio2008@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

path_namespace = "api/v1/"

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # Apps
    path(f"{path_namespace}authentication/", include("authentication.urls")),
    path(f"{path_namespace}employees/", include("employee.urls")),
    path(f"{path_namespace}clients/", include("clients_parking.urls")),
    path(f"{path_namespace}cars/", include("cars.urls")),
    path(f"{path_namespace}vacancies/", include("vacanciens.urls")),
    path(f"{path_namespace}parking/", include("parking.urls")),
    path(f"{path_namespace}reporting/", include("reporting.urls")),
    # swagger
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]


admin.AdminSite.site_header = "Park Easy"
admin.AdminSite.site_title = "Park Easy"
