from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static

urlpatterns = [
    path('anything-but-admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
]

#  if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
