from django.urls import path
from . import views

app_name = 'advertising'

urlpatterns = [
    path('', views.index, name='advertising_index'),
]
