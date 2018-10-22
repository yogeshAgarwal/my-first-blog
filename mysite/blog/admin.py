from django.contrib import admin
from .models import Post, Comment, PostAdmin, CommentAdmin
# from adminfilters.models import Post
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin )

# class PostAdmin(admin.ModelAdmin):
#     list_display =('title', 'published_date')
