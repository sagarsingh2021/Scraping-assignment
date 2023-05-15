from django.urls import path
from .views import UniversityList

urlpatterns = [
    path('universities/', UniversityList.as_view()),
]
