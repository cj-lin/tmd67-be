"""tmd67_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from strawberry.django.views import AsyncGraphQLView

from tmd67_be.api import views
from tmd67_be.api.schema import schema

router = routers.DefaultRouter()
router.register(r"paths", views.ListPathView)
router.register(r"projects", views.ListProjectView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include('tmd67_be.ac.urls')),
    path("", include(router.urls)),
    path("graphql/", AsyncGraphQLView.as_view(schema=schema)),
]
