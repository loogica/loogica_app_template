import logging

from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, redirect
from django.views.decorators.http import require_http_methods

log = logging.getLogger(__name__)


def _rr(request, template_name, data):
    return render_to_response(template_name, data, RequestContext(request))


@require_http_methods(['GET'])
def home(request):
    return _rr(request, "index.html", {})
