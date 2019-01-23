from import_export import resources
from .models import ExcelFile

class ExcelResource(resources.ModelResource):
    class Meta:
        model = ExcelFile