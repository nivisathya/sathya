from django.conf.urls import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'chatbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sathya/', include('sathya.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
