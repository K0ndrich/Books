"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# default django
from django.contrib import admin
from django.urls import path, include

# django rest
from rest_framework.routers import SimpleRouter

# my_project
from store.views import BookViewSet, auth

# создаем маршрутизатор url-путей для нашего API
router = SimpleRouter()
router.register(r"book", BookViewSet)  # -> http://127.0.0.1:8000/book/?format=json

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("social_django.urls", namespace="social")),
    path("auth/", auth),
]

# router.urls хранит внутри себя дефолтные url-пути и которые добавили через router.register
urlpatterns += router.urls
