from django.contrib import admin
# Register your models here.
from .models import harvest_type, crops, sell_harvested_crops, buy_harvested_Crop
# Register your models here.
admin.site.register(harvest_type)
admin.site.register(crops)
admin.site.register(sell_harvested_crops)
admin.site.register(buy_harvested_Crop)
