from django.contrib import admin

# Register your models here.
from report.models import *

admin.site.register(ReportRequest)
admin.site.register(ReportDefinition)