from .views import index
from django.urls import path
from .import views
from .views import index
urlpatterns=[
    path('', views.index, name='index'),
    path('Books/', views.booklist.as_view(), name='Book'),
    path('Books/<int:pk>', views.Detail.as_view(), name='detail'),
    path('authors/', views.authorList.as_view(), name='authorList'),
   path('authors/<int:pk>', views.author_detail.as_view(), name='author_detail'),
   path('sess/', views.sess, name='sess'),
  path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),


]
