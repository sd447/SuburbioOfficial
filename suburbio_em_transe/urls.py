
from django.contrib import admin
from django.urls import path
from app_suburbio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]