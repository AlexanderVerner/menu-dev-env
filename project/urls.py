from django.contrib import admin
from django.urls import path, include
from .views import first_page, checkout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page, name='home'),
    path('api/', include('menu.urls')),
    path('checkout/', checkout, name = 'checkout'),
    path('checkout/admin', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
