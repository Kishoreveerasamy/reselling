from django.urls import path
from . import views  # ✅ correct way — dot means same folder

urlpatterns = [
     path('', views.home_view, name='home'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('post/', views.post_ad, name='post_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('login/', views.login_view, name='login'),
]


from django.urls import path
from homenix import views

urlpatterns = [
    path('post/', views.post_ad, name='post_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('', views.home_view, name='home'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),  # ✅ THIS
    path('register/', views.register_view, name='register'),
    path('post/', views.post_ad, name='post_ad'),
    path('delete/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('logout/', views.logout_view, name='logout'),

]