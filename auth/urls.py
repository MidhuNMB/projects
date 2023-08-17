"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('createac1/',views.createac1),
    path('createac2/',views.createac2),
    path('login1/',views.login1),
    path('admin1/',views.admin1),
    path('user1/',views.user1),
    #admin
    path('addcake1/',views.addcake1),
    path('addcake2/',views.addcake2),
    path('viewcaketbl/',views.viewcaketbl),

    path('delete1/<int:id>',views.delete1),
    path('update1/<int:id>',views.update1),
    path('updatecake/<int:id>',views.updatecake),
    path('viewuser/',views.viewuser),
    path('logout/',views.logout)


]