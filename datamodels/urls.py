from django.urls import path
from .views import DataListView


urlpatterns = [
    path('data/', DataListView.as_view(), name="data"),
]