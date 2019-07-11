from django.shortcuts import render

from .models import Post,BigCategory,Tag

from django.views import generic
from .forms import SearchForm, BlogSearchFormSet
from django.db.models import Q

# Create your views here.

#Post List 取得 一覧取得
class PostList(generic.ListView):

    paginate_by = 10
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



def index(request):
    form = SearchForm(request.POST or None)
    tag_list=Tag.objects.all()
    if request.method == 'POST':
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')


        post_list=Post.objects.filter(
            Q(bigtitle__contains=keyword)|
            Q(bigtext__contains=keyword)
        )

        if (post_list.count()==0):
            return render(request, 'mymemoblog/search.html', {'keyword':keyword,'form':form,'tag_list':tag_list})
        else:
            context={
                'keyword':keyword,
                'form':form,
                'post_list':post_list,
                'tag_list': tag_list
            }
            return render(request, 'mymemoblog/search.html', context)

    else:
        return render(request,'mymemoblog/search.html',{'form':form,'tag_list':tag_list})








