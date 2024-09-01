from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'text')

    def author(self, obj):
        return obj.author.email

    author.short_description = 'Автор'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('text',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
