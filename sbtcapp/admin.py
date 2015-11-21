from django.contrib import admin

from sbtcapp import models

class GalleryAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Gallery,GalleryAdmin)
# Register your models here.
