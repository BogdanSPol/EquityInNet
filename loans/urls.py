from django.urls import path
from . import views

app_name = 'loans'

urlpatterns = [
    path('', views.index, name='loans_index'),
    path('<int:loans_id>/', views.detail, name='detail'),
]