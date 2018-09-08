from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import reverse_lazy
from django.contrib.auth.views import (
	LoginView,
	LogoutView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordChangeView,
	PasswordChangeDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView
)

urlpatterns = [
	              url(r'^admin/', include(admin.site.urls)),
	              url(r'^', include('target.frontend.errors.urls')),
	              url(r'^login/$', LoginView.as_view(template_name='auth/login.html'), name='login'),
	              url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout')
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + staticfiles_urlpatterns()
