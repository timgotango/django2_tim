from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name = 'detail'), # path converter을 다음 인자인 함수에 넣어주어 url 요청되는 것.
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('<int:blog_id>/delete', views.delete, name = 'delete'),
    path('<int:blog_id>/edit', views.edit, name = 'edit'),
    path('<int:blog_id>/update', views.update, name='update'),
    path('introduce/', views.introduce, name = 'introduce'),
]
