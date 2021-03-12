from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
    path('create',index),
    path('palace/<str:user>',index),
    path('versions',index),
    path('about',index),
    path('about-palace', index),
    path('v1',index),
    path('v2',index), 
    path('v3',index),
]
