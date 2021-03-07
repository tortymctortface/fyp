from django.urls import path
from .views import PalaceView,CreatePalaceView

urlpatterns = [
    path('palace', PalaceView.as_view()),
    path('create-palace',CreatePalaceView.as_view())
]