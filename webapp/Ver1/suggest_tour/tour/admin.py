from django.contrib import admin
from .models import TourlistSite,TourlistTraffic,AnalysisReseult

# Register your models here.
admin.site.register(TourlistSite)
admin.site.register(TourlistTraffic)
admin.site.register(AnalysisReseult)