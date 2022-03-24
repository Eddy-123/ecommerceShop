from unicodedata import name
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail
from django.conf.urls.static import static
from shop import settings
from accounts.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('signup/', signup, name='signup')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
