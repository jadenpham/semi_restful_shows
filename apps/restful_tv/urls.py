from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index), #render
    url(r'^shows/new$', views.new_show), #render
    url(r'^shows/(?P<show_id>\d+)$', views.show), #render newly created show, has to match with the return redirect(/shows/show_info.id)
    url(r'^shows/(?P<show_id>\d+)/edit', views.edit), #render edit page
    url(r'^shows/(?P<show_id>\d+)/update', views.update), #process update info
    url(r'^create$', views.create), #process new show form
    url(r'^shows/(?P<show_id>\d+)/delete', views.delete), #delete selected show
]