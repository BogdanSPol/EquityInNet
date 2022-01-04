from django.urls import path
from . import views

app_name = 'icos'

urlpatterns = [
    path('', views.index, name='icos_index'),
    path('<int:icos_id>/', views.detail, name='detail'),
]