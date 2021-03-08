from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
    path('create',index),
    path('palace/<str:user>',index),
    path('versions',index),
    path('about',index)
]
