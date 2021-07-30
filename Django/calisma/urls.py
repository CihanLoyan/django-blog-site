from django.contrib import admin
from django.urls import path, include
from uygulama1_post.views import *
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  #localhost:8000

    #UYGULAMA
    path("uygulama1_post/", include("uygulama1_post.urls")),

    #ÜYELİK
    path("login", login_view),
    path("register", register_view),
    path("logout", logout_view)
 ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)