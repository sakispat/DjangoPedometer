from django.urls import path
from . import views

app_name = 'steps'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('chart/', views.chart, name='chart'),
    path('ajax-chart/', views.ajax_chart, name='ajax_chart'),
]
