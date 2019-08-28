"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, \
    PasswordResetDoneView, LoginView, logout_then_login
from django.urls import include

from colegio import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('apps.principal.urls')),
    url(r'^registro/', include('apps.usuarios.urls')),
    url(r'^alumnos/', include('apps.alumnos.urls')),
    url(r'^maestros/', include('apps.maestros.urls')),

    # Password reset
    url(r'^password_reset/', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_ \-]+)/(?P<token>.+)/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    url(r'logout/', logout_then_login, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
