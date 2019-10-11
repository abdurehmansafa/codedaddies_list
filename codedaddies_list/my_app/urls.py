from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new__search', views.new__search, name='new__search')

]

