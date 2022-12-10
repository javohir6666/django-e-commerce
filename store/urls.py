from django.urls import path
from .views import index
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('collections/', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionView, name='collectionView'),
    path('collections/<str:category_slug>/product/<str:slug>', views.productView, name='productView'),
]
