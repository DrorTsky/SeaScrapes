from django.urls import path
from . import views

urlpatterns = [
    path('', views.sea_info_view, name='index'),
    path('sea_info/', views.sea_info_view, name='sea_details'),
    path('wave_info/', views.wave_view, name='wave_forecast'),
    path('forecast/', views.forecast_view, name='forecast'),
]