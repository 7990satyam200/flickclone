# Neccessary imports of models, forms and django-inbuit classes
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import ListView, DetailView
from .models import harvest_type, crops
from .forms import SaleForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


class sale_crop_proceeds(ListView):
    """
    Generic class-based view listing type of crops for assist in make sell to current Farmer.
    """
    model = harvest_type
    template_name = 'sale_crop_proceeds.html'



def my_crop(request, pk):
    """
    View function for choosing list of general type of crops such as Rabi, Kharif
    """
    harvest = harvest_type.objects.get(pk=pk)
    return render(request, 'crops.html', {'harvest':harvest})

def search_selling(request):
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
    return render_to_response("search_selling.html", {
        "results": results,
        "query": query
    })

@login_required
def sellCrop(request, pk, topic_pk):
    """
    View function for choosing specific type of crops such as sugarcane,tea
    and then accepting details regarding sale.
    finally this function redirects to market page where farmers can see sale live.
    """
    harvest = harvest_type.objects.get(pk = pk)
    crop = get_object_or_404(crops, crop_harvest_type__pk=pk, pk = topic_pk)
    if request.method =='POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale= form.save(commit=False)
            sale.crops = crop
            sale.save()
            return redirect('market', pk=topic_pk)  # TODO: redirect to the created topic page

    else:
        form =SaleForm()
    return render(request, 'sell_crops.html', {'crop':crop, 'harvest':harvest, 'form':form})
