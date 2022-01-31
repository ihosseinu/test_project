from django.urls import path
from .views import ContactViews

urlpatterns = [
    path('', ContactViews.as_view(), name='home'),
    path('<str:phone_number>', ContactViews.as_view()),
]