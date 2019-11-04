from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen


url = 'https://www.downtoearth.org.in/category/agriculture/news'
# Create your views here.
def myblog(request):
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

    return render(request, 'home.html', {'combined': combined })
