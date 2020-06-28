from django.contrib import admin
from django.urls import path
from bot import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('count/',views.answer,name='answer'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
