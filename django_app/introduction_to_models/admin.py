from django.contrib import admin

from .models import Post, Comment, User, Tag
from .models import Person

admin.site.register(Person)
# admin.site.register(Post, Comment, User, Tag)