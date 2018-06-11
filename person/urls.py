from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^photo/(\d+)', views.single_photo, name = 'myPhoto'),
    url(r'^search/', views.search_results, name = 'search_results'),

]
