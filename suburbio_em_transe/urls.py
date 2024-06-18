from django.contrib import admin
from django.urls import path
from app_suburbio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastrarevento/', views.cadastrarevento, name='cadastrarevento'),
    path('SignUp/', views.cadastro, name='cadastro'),
    path('Login/', views.login_view, name='login'),
    path('/', views.index_logged_in, name='index_logged_in'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
