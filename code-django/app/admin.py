from django.contrib import admin

from .models import file

# Register your models here.
# admin.site.register(file)


@admin.register(file)
class fileAdmin(admin.ModelAdmin):
    list_display = ('nameOfFile', 'nameOfLectures')
    ordering = ('nameOfFile',)
    search_fields = ('nameOfFile', 'nameOfLectures')
