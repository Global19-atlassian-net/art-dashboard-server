from django.conf.urls import url
from .views import  BuildView

urlpatterns = [
    url(r'^$', BuildView.as_view(), name='build_view'),
]
