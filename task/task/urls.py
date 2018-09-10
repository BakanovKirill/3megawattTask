"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import debug_toolbar

from django.contrib import admin
from django.urls import path, include

from task.views import (
    SitesList,
    summary,
    summary_average,
    SiteDetail,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    # Task app urls
    path('sites/<int:pk>/', SiteDetail.as_view(), name='site_detail'),
    path('sites/', SitesList.as_view(), name='sites_list'),
    path('summary/', summary, name='summary'),
    path('summary-average/', summary_average, name='summary_average'),
]
