from django.urls import path

from fitbox.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
