from django.http import HttpResponse
from django.core.cache import cache
from django.template import loader
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import time


def homepage_view(request):
    """serves file system caching"""
    cache.set("my_value", "custom data", 30)
    get_cached_value = cache.get("my_value")
    return render(request, 'blog/home.html', {"cached_val": get_cached_value})


@cache_page(60 * 1) # 60 seconds * 1 = 1 minute
def second_page_view(request):
    """per-view cache, returns cached response as this function takes little longer
    to execute. Starts caching from 2nd request onwards."""

    # mimic some long operation
    time.sleep(2)
    
    data = "content for template, updated!"
    return render(request, 'blog/second_page.html', {"data": data})