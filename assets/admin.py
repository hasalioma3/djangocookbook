from django.contrib import admin
from .models import Categories, Assets


admin.site.site_header = "Naivas Assets Admin"
admin.site.site_title = "Naivas Admin Portal"
admin.site.index_title = "Welcome to Naivas Assets Portal"

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class AssetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'created', 'updated')
    search_fields = ('name', 'description', 'category__name', 'created', 'updated')
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Assets, AssetsAdmin)


