from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home1/', views.home1, name='home1'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('contact/', views.contact_view, name='contact'),
]
