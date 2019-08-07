from django.urls import path
from . import views


app_name = 'feedback'
urlpatterns = [
    path('', views.post_new, name='post_new'),
    path('post_confirm/', views.post_confirm, name='post_confirm'),
    path('feedbacks/', views.post_list, name='post_list'),
]