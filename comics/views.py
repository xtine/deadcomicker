from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.template import RequestContext

from comics.models import Comic

def index(request):
    comics = Comic.objects.all().order_by('-id')
    context = RequestContext(request)
    return render_to_response('index.html', {'comics' : comics}, context_instance=context)
