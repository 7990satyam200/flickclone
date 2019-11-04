from django.urls import path
from .views import buy_crop_proceeds, buy_crop, market, search, seller_buy, searchhome

urlpatterns =[
        path('buy_harvest', buy_crop_proceeds.as_view(), name= 'buy_crop_proceeds'),
        path('buy/<int:pk>', buy_crop, name= 'buy_crop'),
        path('market/<int:pk>/', market, name = 'market' ),
        path('search/', search, name='search'),
        path('searchs/', searchhome, name='searchhome'),
        path('seller/<int:pk>/crops/<int:topic_pk>/', seller_buy, name = 'seller_buy'),
        ]
