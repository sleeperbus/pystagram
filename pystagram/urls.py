from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photo/(?P<photo_id>\d+)$', 'photo.views.single_photo', name='view_single_photo'),
    # url(r'^photo/upload/$', 'photo.views.new_photo', name='new_photo'),
    # url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login', kwargs={'template_name':'login.html'}),
    # url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='logout'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  # urlpatterns += static('static_files', document_root=settings.MEDIA_ROOT)


