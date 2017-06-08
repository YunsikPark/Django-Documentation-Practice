from django.contrib import admin

from .models import Post, Comment, User, Tag, PostLike
from .models import Person

admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(PostLike)
