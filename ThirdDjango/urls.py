"""SecondDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ThirdDjango.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', welcome),

    url(r'^form-post/', search),
    url(r'^search-post/', search_post),

    url(r'^form-get/', search),
    url(r'^search-get/', search_get),

    url(r'^login-session/', login),
    url(r'^login-validate/', login_validate),
    url(r'^keep-online/', keep_online),

    url(r'^test-cookies/', test_cookies),

    url(r'test-json/', test_json),

    url(r'^handle-upload/', handle_upload),
    url(r'^upload/', upload),
]
