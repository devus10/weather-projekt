from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^miasto/$', views.popup_miasto, name="popup_miasto"),
    url(r'^wspolrzedne/$', views.popup_wspolrzedne, name="popup_wspolrzedne"),
]