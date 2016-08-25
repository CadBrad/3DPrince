from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from allauthdemo.demo.forms import NewUpload, ConfigUpload

@login_required
def member_index(request):
    return render_to_response("member/member-index.html", RequestContext(request))

@login_required
def member_config(request):
    return render_to_response("visitor/configupload.html", RequestContext(request))

