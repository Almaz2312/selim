"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# schema_view = get_schema_view(
#     openapi.Info(
#         title = 'Selim',
#         description = 'Python_back',
#         default_version = 'v1',
#     ),
#     public = True
# )
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Selim",
        description="Python_back",
        default_version="v1",
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("news.urls")),
    path("api/v1/", include("other.urls")),
    path("docs/", schema_view.with_ui("swagger")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
