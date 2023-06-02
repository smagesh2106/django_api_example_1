"""
URL configuration for django_project project.

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
from django.urls import path, include # new
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView, # new
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("books.urls")), # new
    path("api/v1/", include("apis.urls")), # new
    path("api-auth/", include("rest_framework.urls")), # new
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")), # new
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")), # new
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view( url_name="schema"), name="swagger-ui"), # new
]

