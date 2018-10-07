from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    
# 注册
    url(r'^register/$',views.register,name='register'),

    url(r'^login/$',views.login,name='login'),
    
    url(r'^logout/$',views.quit,name='logout')
]