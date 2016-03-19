from django.conf.urls import url
from . import views # import current views package

urlpatterns = [
	url(r'^$', views.index, name='index')
]