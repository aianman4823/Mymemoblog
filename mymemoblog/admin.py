from django.contrib import admin

from .models import BigCategory,SmallCategory,Tag,Post,BlogBlock,Comment,Reply

# Register your models here.

admin.site.register(BigCategory)
admin.site.register(SmallCategory)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(BlogBlock)
admin.site.register(Comment)
admin.site.register(Reply)
