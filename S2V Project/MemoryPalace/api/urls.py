from django.urls import path
from .views import PalaceView,CreatePalaceView, GetPalaceView, RecentPalaceView

urlpatterns = [
    path('palace', PalaceView.as_view()),
    path('create-palace',CreatePalaceView.as_view()),
    path('get-palace',GetPalaceView.as_view()),
    path('recent-palace',RecentPalaceView.as_view())
]