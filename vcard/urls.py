from django.urls import path
from .views import vcard
urlpatterns = [
    path('', vcard.as_view() , name="vcard"),
]
