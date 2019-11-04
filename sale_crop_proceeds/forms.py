from django.forms import ModelForm, ImageField
from .models import harvest_type, crops, sell_harvested_crops
from django.contrib.auth.models import User


class SaleForm(ModelForm):
    """
    Django based forms Sale Form for rendering form from models on templates
    """
    class Meta:
        model = sell_harvested_crops
        fields = ('quantity', 'harvest_variety', 'h_description', 'quality', 'sold_by', 'farm_image')
