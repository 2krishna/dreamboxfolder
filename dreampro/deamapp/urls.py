from django.urls import path
from deamapp import views

urlpatterns = [
    
    path('create/', views.create_csvmap,name='create'),
    path('list/', views.list_csvview,name='list'),
]