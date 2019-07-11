from django.shortcuts import render

from .models import Post,BigCategory,Tag

from django.views import generic

# Create your views here.

#Post List 取得 一覧取得
class PostList(generic.ListView):
    model = Post
    template_name = 'mymemoblog/blog_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'tag_list':Tag.objects.order_by('name'),
            'more_context':Tag.objects.all(),
        })
        post_list=Post.objects.all().order_by('-created_at')[:10]
        return context


#Post Detail 取得 詳細なブログを獲得する
class PostDetail(generic.DetailView):
    queryset = Post.objects.all()
    template_name = 'mymemoblog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'tag_list':Tag.objects.order_by('name'),
            'more_context':Tag.objects.all(),
        })
        return context


