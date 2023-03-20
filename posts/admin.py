from django.contrib import admin

# Register your models here.
from .models import Author, Category, Post, Comment 


class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "meta",)
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)



