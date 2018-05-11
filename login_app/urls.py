
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.userLogin, name='index'),
    url(r'^login_app/$', views.authenticateUser, name='login_app'),
    url(r'^privacy/$', views.privacy_view, name='privacy'),
    url(r'^signup/$',views.signup, name = 'signup'),
    url(r'^registeruser/$',views.registeruser, name = 'registeruser'),
    url(r'^logout/$',views.user_logout, name = 'logout'),

]