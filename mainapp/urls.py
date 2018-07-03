from django.urls import path
from mainapp import views

urlpatterns = [
    path('sign/', views.sign, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('postsign/', views.postsign, name='login'),
    path('schoolform/', views.schoolform, name='schoolform'),

]