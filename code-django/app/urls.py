from django.urls import path
from . import views

#from app.views import mainPage, storeFile, deleteFile

urlpatterns = [
    path('', views.home, name="home"),
    # path('main/', mainPage),
    # path('store/', storeFile),
    # # <int:file_id> is replaced by the primary key of the data
    # path('delete/<int:file_id>/', deleteFile),
    path('database/', views.database, name="output_database"),
]
