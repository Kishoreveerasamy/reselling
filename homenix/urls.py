# homenix/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties, name='properties'),
    path('post-ad/', views.post_ad, name='post_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('login/', views.login_view, name='login'),

    path('register/', views.register_view, name='register'),

    path('logout/', views.logout_view, name='logout'),

]
