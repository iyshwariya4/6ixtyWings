from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main.html', views.say_hello),
    path('register.html',views.register, name='register'),
    path('collections.html',views.collections, name='collections'),

    path('collections/<str:slug>',views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('collections/<str:slug>',views.collectionsview, name='collectionsview')



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

