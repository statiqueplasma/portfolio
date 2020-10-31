from django.urls import path
from .views import HomeView, ServiceView
app_name='portfolio'

urlpatterns = [
    path('home/', HomeView.as_view() , name="home"),
    path('services/<int:pk>', ServiceView.as_view(), name='services'),
]
