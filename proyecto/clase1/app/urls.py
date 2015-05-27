from django.conf.urls import patterns, url, include

urlpatterns = patterns('app.views',

	#este es mi primer index
	url(r'^$', 'index'),


	)