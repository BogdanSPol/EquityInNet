from django.urls import path
from . import views

app_name = 'equities'

urlpatterns = [
    path('', views.index, name='equities_index'),
    path('<slug:equities_slug>/', views.detail, name='detail'),
]