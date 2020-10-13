from django.shortcuts import render
from django.views import generic
# Create your views here.

from SeaInfo import utils


def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def sea_info_view(request):
    wave_info = utils.get_wave_info()
    context = {"wave_info": wave_info}
    return render(request, 'SeaInfo/sea_details.html', context)

def wave_view(request):
    map_info = utils.get_mediterranean_map()
    context = {"map_info": map_info}
    return render(request,'SeaInfo/wave_forecast.html',context)

def forecast_view(request):
    forecast_info = utils.get_forecast()
    context = {"forecast_info": forecast_info}
    return render(request,"SeaInfo/forecast.html",context)
