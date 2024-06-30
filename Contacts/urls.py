from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path("create",views.create,name='create'),
    path("search",views.search,name='search'),
    path("removed",views.removed,name='removed'),
]