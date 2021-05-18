

"""timproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views # import app이름.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home"),
    path('blog/<int:blog_id>/', blog.views.detail, name = 'detail'), # path converter을 다음 인자인 함수에 넣어주어 url 요청되는 것.
    path('blog/new/', blog.views.new, name = 'new'),
    path('blog/create/', blog.views.create, name = 'create'),
    path('blog/<int:blog_id>/delete', blog.views.delete, name = 'delete'),
    path('blog/<int:blog_id>/edit', blog.views.edit, name = 'edit'),
    path('blog/<int:blog_id>/update', blog.views.update, name='update'),
    path('blog/introduce/', blog.views.introduce, name = 'introduce'),
]
