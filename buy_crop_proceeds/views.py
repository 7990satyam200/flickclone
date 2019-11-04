from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import ListView, DetailView
from sale_crop_proceeds.models import harvest_type, crops, sell_harvested_crops
from django.db.models import Q
from .forms import seller_buy_form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
class buy_crop_proceeds(ListView):
    """
    Generic class-based view listing type of crops for assisting in buying current WholeSaler.
    """
    model = harvest_type
    template_name = 'buy_crop_proceeds.html'



def buy_crop(request, pk):
    """
    View function for choosing list of general type of crops such as Rabi, Kharif for assisting in buying
    """
    harvests = harvest_type.objects.get(pk=pk)
    return render(request, 'buy_crops.html', {'harvests':harvests})


def market(request,  pk):
    """
    View function for displaying list of sale of specific crop of made by
    farmers, from there WholeSaler can proceed to place an order against specific bid.
    """
    my_crop = crops.objects.get(pk=pk)
    sold = sell_harvested_crops.objects.filter(crops=pk)
    return render(request, 'market.html', {'sold':sold, 'my_crop':my_crop})

def search(request):
    """
    View function for querying specific type of crops such as sugarcane, wheat
    allowing farmers to sell their crops
    """
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(crop_name__icontains=query)
)
        results = crops.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search_buying.html", {
        "results": results,
        "query": query
    })

def searchhome(request):
    harvest_types = harvest_type.objects.all()
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(crop_name__icontains=query)
)
        results = crops.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search_buying.html", {
        "results": results,
        "query": query,
        "harvest_types":harvest_types
    })

@login_required
def seller_buy(request, pk, topic_pk):
    """
    View function for choosing specific type of crops such as sugarcane,tea
    and then accepting details regarding sale.
    finally this function redirects to market page where farmers can see sale live.
    """
    brought = False
    crop = crops.objects.get(pk= pk)
    sold_crop = get_object_or_404(sell_harvested_crops, crops=pk, pk = topic_pk)
    if request.method =='POST':
        form = seller_buy_form(request.POST)
        if form.is_valid():
            sale= form.save(commit=False)
            sale.buy_crops = sold_crop
            sale.buyer = request.user
            sale.save()
            brought = True
    else:
        form =seller_buy_form()
    return render(request, 'buy_crop_form.html', {'sold_crop':sold_crop, 'form':form, 'brought':brought, 'crop':crop})
