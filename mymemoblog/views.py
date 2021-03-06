from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from django.contrib.sitemaps import ping_google

from .models import Post,SmallCategory,Tag,Comment,Reply
from django.views import View

from django.views import generic
from .forms import SearchForm
from django.db.models import Q

# Create your views here.

def paginate_query(request, queryset, count):
  paginator = Paginator(queryset, count)
  page = request.GET.get('page')
  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)
  return page_obj

#Post List 取得 一覧取得
class PostList(generic.ListView):

    paginate_by = 10
    model = Post
    template_name = 'mymemoblog/blog_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'category_list':SmallCategory.objects.order_by('name'),
            'tag_list':Tag.objects.order_by('name'),
            'more_context':Tag.objects.all(),
        })
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_publick=True).order_by('-created_at')


#Post Detail 取得 詳細なブログを獲得する
class PostDetail(generic.DetailView):
    queryset = Post.objects.all()
    template_name = 'mymemoblog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'tag_list':Tag.objects.order_by('name'),
            'more_context':Tag.objects.all(),
            'category_list': SmallCategory.objects.order_by('name'),
        })
        return context



def index(request):
    form = SearchForm(request.POST or None)
    tag_list=Tag.objects.order_by('name')
    category_list= SmallCategory.objects.order_by('name')
    if request.method == 'POST':
        form.is_valid()
        keyword = form.cleaned_data.get('keyword')


        post_list=Post.objects.filter(
            Q(bigtitle__contains=keyword)|
            Q(bigtext__contains=keyword)
        ).filter(is_publick=True).order_by('-created_at')

        if (post_list.count()==0):
            return render(request, 'mymemoblog/search.html', {'keyword':keyword,
                                                              'form':form,
                                                              'tag_list':tag_list,
                                                              'category_list':category_list})
        else:
            context={
                'keyword':keyword,
                'form':form,
                'post_list':post_list,
                'tag_list': tag_list,
                'category_list': category_list,
            }
            return render(request, 'mymemoblog/search.html', context)

    else:
        return render(request,'mymemoblog/search.html',{'form':form,'tag_list':tag_list,'category_list':category_list})


class PostTagView(View):

    def get(self,request,pk):
        tag=Tag.objects.get(pk=pk)
        tag_list=Tag.objects.order_by('name')
        category_list=SmallCategory.objects.order_by('name')
        post_list=Post.objects.filter(tag=tag).filter(is_publick=True).order_by('-created_at')
        page_obj=paginate_query(request,post_list,10)
        context = {
            'tag_list':tag_list,
            'tag': tag,
            'post_list': post_list,
            'category_list':category_list,
            'page_obj':page_obj,
        }


        return render(request,'mymemoblog/blog_tag_list.html',context)

class PostSmallCategory(View):
    def get(self,request,pk):
        smallcategory=SmallCategory.objects.get(pk=pk)
        category_list=SmallCategory.objects.order_by('name')
        post_list = smallcategory.small_category.filter(is_publick=True).order_by('-created_at')
        tag_list=Tag.objects.order_by('name')
        page_obj=paginate_query(request,post_list,10)
        context={
            'smallcategory':smallcategory,
            'post_list':post_list,
            'tag_list':tag_list,
            'category_list':category_list,
            'page_obj':page_obj
        }

        return render(request,'mymemoblog/blog_category_list.html',context)



class CommentView(generic.CreateView):
    #コメント投稿
    model = Comment
    fields = ('name','text')
    template_name = 'mymemoblog/comment_form.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'tag_list':Tag.objects.order_by('name'),
            'more_context':Tag.objects.all(),
            'category_list': SmallCategory.objects.order_by('name'),
        })
        return context

    def form_valid(self, form):
        post_pk=self.kwargs['pk']
        post=get_object_or_404(Post,pk=post_pk)

        #紐づく記事を設定する
        comment=form.save(commit=False)
        comment.target=post
        comment.save()

        #記事詳細にリダイレクト
        return redirect('mymemoblog:post_detail',pk=post.pk)


class ReplyView(generic.CreateView):
    #返信作成view
    model = Reply
    fields = ('name','text')
    template_name = 'mymemoblog/comment_form.html'

    def form_valid(self, form):
        comment_pk=self.kwargs['pk']
        comment=get_object_or_404(Comment,pk=comment_pk)

        #ひもづくコメントを設定
        reply=form.save(commit=False)
        reply.target=comment
        reply.save()


        #記事詳細にリダイレクト
        return redirect('mymemoblog:post_detail',pk=comment.target.pk)


@login_required
def ping(request):
    try:
        url=resolve('sitemap')
        ping_google(sitemap_url=url)
    except Exception:
        raise
    else:
        return redirect('mymemoblog:post_list')



