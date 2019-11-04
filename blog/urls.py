from django.urls import path
from .views import myblog


urlpatterns = [
    path('news', myblog, name = 'myblog')
]
