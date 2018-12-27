"""charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from charts import urls
from .views import HomeView, get_data, ChartData


app_name = 'charts'

urlpatterns = [
    path('charts/', HomeView.as_view(), name='charts'),
    path('charts/api/data/', get_data, name='api-data'),
    path('charts/api/chart/data/', ChartData.as_view()),
    # path('charts/api/chart/data/', ChartData1.as_view()),

]
