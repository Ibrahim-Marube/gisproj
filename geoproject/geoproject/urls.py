from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('location_list/', views.location_list, name='location_list'),
    path('search_results/', views.location_search, name='search_results'),
]
