from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<slug:slug>/', views.job_detail, name='job_detail'),
    path('bookmark/<int:job_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('my-bookmarks/', views.user_bookmarks, name='user_bookmarks'),
]