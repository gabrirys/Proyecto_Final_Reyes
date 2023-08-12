from django.contrib import admin
from app_blog.models import Articulo

#admin.site.register(Articulo)
@admin.register(Articulo)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor")
    list_filter = ("autor",)
    list_per_page = 6
    search_fields = ("titulo", "autor")
    