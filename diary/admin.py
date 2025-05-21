from django.contrib import admin
from .models import Entry, Category, Tag

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'category')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags')

admin.site.register(Category)
admin.site.register(Tag)