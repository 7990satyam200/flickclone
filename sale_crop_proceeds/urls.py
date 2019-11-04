from django.urls import path
from .views import sale_crop_proceeds, my_crop, sellCrop, search_selling


urlpatterns =[
        path('sale', sale_crop_proceeds.as_view(), name= 'sale_crop_proceeds'),
        path('w/<int:pk>', my_crop, name= 'my_crop'),
        path('w/<int:pk>/crops/<int:topic_pk>/', sellCrop, name = 'sellCrop' ),
        path('search_selling/', search_selling, name='search_selling'),
        ]
