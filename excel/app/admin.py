from django.contrib import admin
from app.models import ExcelFile
# Register your models here.


class ExcelFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(ExcelFile, ExcelFileAdmin)
