from django.conf import settings
from django.conf.urls import url

from .views import ErrorView

handler500 = ErrorView.as_view(error=500)
handler400 = ErrorView.as_view(error=400)
handler403 = ErrorView.as_view(error=403)
handler404 = ErrorView.as_view(error=404)

urlpatterns = []

if settings.DEBUG:
	urlpatterns += [
		# Testing 404 and 500 error pages
		url(r'^500/$', ErrorView.as_view(error=500)),
		url(r'^400/$', ErrorView.as_view(error=404)),
		url(r'^403/$', ErrorView.as_view(error=403)),
		url(r'^404/$', ErrorView.as_view(error=404)),
	]