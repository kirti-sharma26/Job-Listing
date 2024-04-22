from django.urls import path
from . import views

app_name = 'job_details'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin1/', views.admin1, name='admin1'),
    path('apply/',views.apply, name='apply')
]
