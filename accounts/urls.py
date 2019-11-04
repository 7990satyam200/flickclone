from django.urls import path, include
from .views import profile, signup, myhome
from django.contrib.auth import views

urlpatterns = [
    #path('signup', user_creation, name = 'signup'),
    path('signup', signup, name = 'signup'),
    path('', myhome, name= 'home'),
    #path('register', register, name= 'register' ),
    path('profile', profile, name = 'profile'),
    path('login', views.LoginView.as_view(), name = 'login'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('logout/', views.LogoutView.as_view(), name='logout' ),

]
