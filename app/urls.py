from . import views
from django.urls import path
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('add',views.add,name="add")
]
