"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include, re_path
from django.views.static import serve

from instagram import settings
from cards import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('new', views.upload_card, name='upload_card'),
    path('profile/<int:user_id>', views.get_user_profile, name='get_user_profile'),
    path('post/<int:post_id>', views.get_post_detail, name='get_post_detail'),

    path('admin/', admin.site.urls),
    path('authorization/', include('authorizations.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, }),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]

