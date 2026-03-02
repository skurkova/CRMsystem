"""
URL configuration for CRMsystem project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from CRMsystem.views import IndexView

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout'),

    # API приложений
    path('products/', include('services.urls')),
    path('ads/', include('advertising_campaigns.urls')),
    path('leads/', include('potential_clients.urls')),
    path('contracts/', include('contracts.urls')),
    path('customers/', include('active_clients.urls'))
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
