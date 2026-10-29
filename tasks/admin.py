from django.contrib import admin

from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('title',)
    readonly_fields = ('created_at',)
    list_select_related = ('author',)
