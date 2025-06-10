from django.contrib import admin
from .models import Information, Service, Message


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'photo', 'created_at', 'updated_at', 'id')
    list_editable = ('photo',)
    search_fields = ('title_uz', 'title_ru')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'picture', 'created_at', 'updated_at', 'id')
    list_editable = ('picture',)
    search_fields = ('title', 'title_ru')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'id')
    search_fields = ('name', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)