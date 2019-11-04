from django.forms import ModelForm, ImageField
from sale_crop_proceeds.models import  buy_harvested_Crop
from django.contrib.auth.models import User


class seller_buy_form(ModelForm):
    class Meta:
        model = buy_harvested_Crop
        fields = ['quantity']
