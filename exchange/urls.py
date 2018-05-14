from django.conf.urls import url
from . import views

app_name = 'exchange'

urlpatterns = [
	url('^exchange/$',views.index, name='index'),
	url('^uploaddata/$',views.upload_data, name='upload_csv'),
]