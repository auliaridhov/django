from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^halamanke2/$', views.halamanke2, name='halamanke2'),
	url(r'^about/$', views.about, name='about'),
	url(r'^offlane/$', views.offlane, name='offlane'),
	url(r'^midlane/$', views.midlane, name='midlane'),
	url(r'^safelane/$', views.safelane, name='safelane')
	]
