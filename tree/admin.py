from django.contrib import admin
from .models import Tree, Branch


# Register your models here.


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title', 'public', 'published')
    list_filter = ('public', 'published')
    ordering = ('public', 'published')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('tree', 'title', 'full_url')
    list_filter = ('created',)
    ordering = ('created',)
