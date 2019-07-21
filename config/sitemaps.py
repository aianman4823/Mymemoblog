from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from mymemoblog.models import Post



class PostSitemap(Sitemap):
    changereq="never"
    priority=0.8

    def items(self):
        return Post.objects.filter(is_publick=True)


    def location(self, obj):
        return reverse('mymemoblog:post_detail',args=[obj.pk])

    def lastmod(self,obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    changereq="daily"
    priority=0.5

    def items(self):
        return ['mymemoblog:post_list','mymemoblog:search']

    def location(self, item):
        return reverse(item)