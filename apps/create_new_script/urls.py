from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.NewScriptView.as_view()),
    url(r'^output/$', views.OutputScriptView.as_view(), name='output'),
]
