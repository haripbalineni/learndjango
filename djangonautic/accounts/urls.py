from django.conf.urls import url,re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup_view, name='signup')
]