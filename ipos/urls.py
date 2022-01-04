from django.urls import path
from . import views

app_name = 'ipos'

urlpatterns = [
    path('', views.index, name='ipos_index'),
    path('<int:ipos_id>/', views.detail, name='detail'),
]