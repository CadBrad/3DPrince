from django.contrib import admin
# Register your models here.
from .models import UploadedFiles, ConfigFiles

class BookAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Category', 'SubCategory')
    list_filter = ('pub_date',)
    date_hierarchy = ('pub_date')
    
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('Printer', 'Plastic', 'creator')


admin.site.register(UploadedFiles, BookAdmin)
admin.site.register(ConfigFiles, ConfigAdmin)