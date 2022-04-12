"""djangoBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

# from app.views import mainPage, storeFile, deleteFile

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.urls')),
    # path('main/', mainPage),
    # path('store/', storeFile),
    # # <int:file_id> is replaced by the primary key of the data
    # path('delete/<int:file_id>/', deleteFile),

    # for login users section
    # for using django own authentication system
    #     path('users/', include('django.contrib.auth.urls')),
    #     path('users/', include('users.urls')),
]

# configure Admin Titles
admin.site.site_header = "Physics Database Homework"
admin.site.site_title = "Physics Database Homework"
admin.site.index_title = "Welcome To The Admin Area"
