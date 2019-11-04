from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from sale_crop_proceeds.models import harvest_type


url = 'https://www.downtoearth.org.in/category/agriculture/news'
# Create your views here.
def home2(request):
    harvests = harvest_type.objects.all()
    source = urlopen(url).read()
    soup = BeautifulSoup(source, "lxml")
    combined = []
    for i in soup.find_all('div', class_='single-news-wrapper'):
        link= i.find('a').get('href')
        title= i.find('a').find('img').get('alt')
        description= i.find('p', class_='content-main').text
        image_link= i.find('a').find('img').get('src')

        my_mini_list = [link, title , description, image_link ]
        combined.append(my_mini_list)

    return render(request, 'apart.html', {'combined': combined, 'harvests':harvests })



# Create your views here.
class home(TemplateView):
    template_name = 'landing-page.html'
