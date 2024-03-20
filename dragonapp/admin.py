from django.contrib import admin
from dragonapp.models import Movies,Categories
# Register your models here.
admin.site.register(Movies)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("category",)}

admin.site.register(Categories,CategoryAdmin)





