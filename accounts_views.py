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


class home(ListView):
    template_name = 'home.html'

@login_required
def myhome(request):
    """
    Dynamic View function for home page of site.
    """
    # Filter the Our_User Model using the user who is currently logged in
    myuser = Our_User.objects.get(user = request.user)
    # Extracting current user city
    city = myuser.city
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    # Making request to weather API with current user city
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    weather = {
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    # Scraping agriculture new website downtoearth
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


def signup(request):
    # Initially False; presume it was a failure until proven otherwise!
    registered = False
    # If HTTP POST, process form data and create an account.
    if request.method =='POST':
        # Grab raw form data - making use of both FormModels.
        user_form = UserForm(data = request.POST)
        profile_form = ProfileForm(data= request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.picture = request.FILES['picture']
            # Now save the model instance
            profile.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            # say registration was successful.
            registered = True
            return redirect('home')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})
