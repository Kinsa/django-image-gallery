from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from gallery.models import PhotoSet


def gallery_detail(request, slug):
    if request.user.is_active:
            can_login = 'True'
    else:
        can_login = 'False'

    gallery = get_object_or_404(PhotoSet, slug=slug)

    return render_to_response('gallery/photoset_detail.html',
        {'object': gallery, 'can_login': can_login},
        context_instance=RequestContext(request))
