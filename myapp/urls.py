from django.urls import path
from .import views


urlpatterns = [
    path('home',views.home,name='home'),
    path('view_product',views.view_product,name ='view_product'),
    path('add',views.add,name='add')
]