"""hedgecrypt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import about, robots_txt, index
from blog.views import home, privacy_policy, terms_conditions

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CategorySitemap, PostSitemap

sitemaps = {"category": CategorySitemap, "post": PostSitemap}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps,}),
    path("robots.txt", robots_txt, name = "robots_txt"),
    path("admin/", admin.site.urls),
    path("about/", about, name="about"),
    path("index/", index, name="index"),
    path("privacy_policy/", privacy_policy, name="privacy_policy"),
    path("terms_conditions/", terms_conditions, name="terms_conditions"),
    path("", include("blog.urls")),
    # path("", frontpage, name="frontpage"),
    path("", home, name="home"),
    # path("register/", include("django.contrib.auth.urls")),
    # path("register/", include("core.urls")),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
