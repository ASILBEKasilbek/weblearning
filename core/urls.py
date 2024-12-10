from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from app.views import home,category_videos
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('category/<int:category_id>/', category_videos, name='category_videos'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
