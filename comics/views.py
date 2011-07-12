from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext, Context
from comics.models import Comic

import random

# function to return context
# for comic navigation links
def nav(comic_id):
    # grab previous comic
    if comic_id > 1:
        prev = comic_id - 1
    else:
        prev = None
    # grab last comic
    if comic_id == Comic.objects.count():
        last = None
    else:
        last = Comic.objects.count()
    # grab next comic
    if comic_id != last:
        next = comic_id + 1
    else:
        next = None
                
    return Context({'last' : last, 'prev' : prev, 'next' : next})

# front page
def index(request):
    comic = Comic.objects.all().order_by('-id')[0]
    
    context = RequestContext(request)
    return render_to_response('comic.html', {'comic' : comic, 'nav' : nav(comic.id)}, context_instance=context)

# comic page
def comic(request, comic_id):
    try:
        c = Comic.objects.get(pk=comic_id)
    except:
        raise Http404
        
    context = RequestContext(request)
    return render_to_response('comic.html', {'comic' : c, 'nav' : nav(int(comic_id))}, context_instance=context)

# random comic
def random_comic(request):
    random_comic_id = str(random.randint(1, Comic.objects.count()))
    
    return HttpResponseRedirect('/comic/' + random_comic_id)

# archive
def archive(request):
    c = Comic.objects.all().values('id', 'title')
    
    context = RequestContext(request)
    return render_to_response('archive.html', {'comics' : c})
    
