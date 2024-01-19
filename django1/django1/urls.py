"""
URL configuration for django1 project.

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
from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter
from mysite import views

from mysite.views import generate_pdf

router = DefaultRouter()
router.register(r'mysite', views.mysiteViewSet)

urlpatterns = [
    path('',views.home_view,name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('login_home/', views.login_home_view, name='login_home'),
    path('register/success/', views.success_view, name='success'),
    path('generate-pdf/', generate_pdf, name='generate_pdf')
]
