from django.urls import path


from .views import PostList,PostDetail,index,PostTagView,PostSmallCategory,CommentView,ReplyView


app_name='mymemoblog'
urlpatterns=[
    path('',PostList.as_view(),name='post_list'),
    path('detail/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('search/',index,name='search'),
    path('tag/<int:pk>/',PostTagView.as_view(),name='post_tag'),
    path('category/<int:pk>/',PostSmallCategory.as_view(),name='post_category'),

    path('comment/<int:pk>/',CommentView.as_view(),name='comment'),
    path('reply/<int:pk>',ReplyView.as_view(),name='reply'),
]