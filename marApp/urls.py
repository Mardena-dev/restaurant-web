from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='homePage'),
    # path('about/', views.about, name='aboutPage'),
     path('reservation/', views.reservation, name='reservationPage'),
    # path('contact/', views.contact, name='contactPage'),
    path('menu/', views.contact, name='menuPage'),

]