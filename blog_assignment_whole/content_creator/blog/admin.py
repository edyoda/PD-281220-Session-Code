from django.contrib import admin
from .models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", )
    prepopulated_fields = {"slug": ("title", )}

# Register your models here.
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
