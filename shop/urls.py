from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/order/', include('order.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/spam/', include('spam.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
