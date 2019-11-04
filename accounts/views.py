from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .forms import SignUpForm, UserForm, UserProfileForm, ProfileForm
from .models import UserProfile, Our_User
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.contrib.auth.decorators import login_required

agriculture_url = 'https://www.downtoearth.org.in/category/agriculture/news'

# Create your views here.

class home(ListView):
    template_name = 'home.html'

@login_required
def myhome(request):
    myuser = Our_User.objects.get(user = request.user)
    city = myuser.city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    weather = {
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    source = urlopen(agriculture_url).read()
    soup = BeautifulSoup(source, "lxml")
    combined = []
    for i in soup.find_all('div', class_='single-news-wrapper'):
        link= i.find('a').get('href')
        title= i.find('a').find('img').get('alt')
        description= i.find('p', class_='content-main').text
        image_link= i.find('a').find('img').get('src')
        my_mini_list = [link, title , description, image_link ]
        combined.append(my_mini_list)

    return render(request, 'landing-page.html', {'myuser':myuser, 'weather':weather , 'combined': combined})



def profile(request):
    queryset = UserProfile.objects.filter(user__username =request.user)
    return render(request, 'profile.html', {'user':queryset})


# def user_creation(request):
#     if request.method =='POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username = username, password = raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form':form})



# def register(request):
# 	registered = False
# 	if request.method =='POST':
# 		user_form = UserForm(data = request.POST)
# 		profile_form = UserProfileForm(data= request.POST)
# 		if user_form.is_valid() and profile_form.is_valid():
# 			user = user_form.save()
# 			user.set_password(user.password)
# 			user.save()
# 			profile = profile_form.save(commit=False)
# 			profile.user = user
#
# 			if 'picture' in request.FILES:
# 				profile.picture = request.FILES['picture']
#
# 			profile.save()
# 			registered = True
# 		else:
# 			print(user_form.errors, profile_form.errors)
# 	else:
# 		user_form = UserForm()
# 		profile_form = UserProfileForm()
# 	return render(request, 'signup.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def signup(request):
    registered = False
    if request.method =='POST':
        user_form = UserForm(data = request.POST)
        profile_form = ProfileForm(data= request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.picture = request.FILES['picture']
            profile.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})
