from django.conf.urls import url
from apps.principal.views import index, register

urlpatterns = [
    url(r'^$', index, name='index'),
]