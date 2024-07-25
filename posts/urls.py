from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<str:ic>',views.post, name='post')
    
]