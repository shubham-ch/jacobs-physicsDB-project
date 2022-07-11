from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


#from app.views import mainPage, storeFile, deleteFile

urlpatterns = [
    path('', views.home, name="home"),
    # path('main/', mainPage),
    # path('store/', storeFile),
    # # <int:file_id> is replaced by the primary key of the data
    # path('delete/<int:file_id>/', deleteFile),
    path('database/', views.database, name="output_database"),
    path('database_followup/<file_id>',
         views.database_followup, name='database-followup'),
    path('add_forms', views.add_forms, name='add-forms'),
    path('search', views.search_database, name='search-database'),
    path('update_database/<file_id>',
         views.update_database, name='update_database'),

    path('delete_data/<file_id>', views.delete_data, name='delete_data'),
    path('download_text', views.download_text, name='download_text'),
    path('download_csv', views.download_csv, name='download_csv'),
    path('download_pdf', views.download_pdf, name='download_pdf'),
    path('filter', views.filter, name='filter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
