from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='homepage'),
    path('day/<key>',views.daysdata,name='homepage'),
]
