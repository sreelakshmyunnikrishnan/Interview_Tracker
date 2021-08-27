"""interviewtracker URL Configuration

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
from intrack import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', views.register),
    path('log/', views.logins),
    path('shad/', views.showadmin),
    path('ent/', views.entry),
    path('shus/', views.showuser),
    path('Delete/<int:id>',views.delint),
    path('Edit/<int:id>',views.edit),
    path('Update/<int:id>',views.update),
    path('alert/',views.alert),
    path('note/',views.note),
    path('notedit/<int:id>',views.notedit),
    path('noteupdate/<int:id>',views.noteupdate),
    path('noteview/',views.shownote),
    path('Delnote/<int:id>',views.delnote),
    path('lt/',views.logouts)

]
