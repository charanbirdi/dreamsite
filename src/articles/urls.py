from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latestarticles$', views.latestarticles, name='latestarticles'),
    url(r'^capacitorsizing', views.capacitorsizing, name='capacitorsizing'),
    url(r'^transformersizing', views.transformersizing, name='transformersizing'),
    url(r'^systemstudy', views.systemstudy, name='systemstudy'),
    url(r'^(?P<id>\d+)/$', views.article, name='article'),
]