from django.conf.urls.defaults import patterns, url

from gallery.models import PhotoSet
from gallery.views import gallery_detail


urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', {'queryset': PhotoSet.objects.all()},
        'gallery_list'),
    url(r'^(?P<slug>[-\w]+)/$', gallery_detail, name='gallery_detail'),
)
