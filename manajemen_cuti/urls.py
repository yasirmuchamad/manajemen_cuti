"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'manajemen_cuti'

urlpatterns = [
    path('cuti', views.listCuti, name='list_cuti'),
    path('cuti/create', views.addCuti, name='add_cuti'),
    path('cuti/approve_cuti/<int:pk>', views.approveCuti, name='approve_cuti'),
    path('cuti/cancel_cuti/<int:pk>', views.cancelCuti, name='cancel_cuti'),
    path('cuti/reject_cuti/<int:pk>', views.rejectCuti, name='reject_cuti'),

    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
