from django.urls import path
from .views import *
from . import views

app_name = 'students'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
]
