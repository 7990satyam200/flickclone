from django.urls import path
from .views import agrinews


urlpatterns = [
    path('news_category', agrinews, name = 'agrinews')
]
