from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^capacitorsizing', views.capacitorsizing, name='capacitorsizing'),
    url(r'^transformersizing', views.transformersizing, name='transformersizing'),
    url(r'^systemstudy', views.systemstudy, name='systemstudy'),
    url(r'^generalarticles/(?P<id>\d+)/$', views.generalarticles, name='generalarticles'),
]