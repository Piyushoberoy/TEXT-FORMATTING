"""Text_Formating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('PageNotFound',views.error_404,name='error_404'),
    path('Welcome', views.home1,name='home1'),
    path('Content/',include('Content.urls')),
    path('Check/',include('Check.urls'),name='check'),
    path('Signup',views.handleSignup,name='signup'),

    path('login',views.login1,name='login'),
    path('Forget_password',views.frgt_pswd,name='frgt_pswd'),
    path('Forget_password_reset',views.frgt_pswd_msg,name='frgt_pswd_msg'),
    path('Register',views.register,name='register'),
    path('Delete',views.del_user,name='delete_user'),

    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
