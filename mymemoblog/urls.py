from django.urls import path


from .views import PostList,PostDetail


app_name='mymemoblog'
urlpatterns=[
    path('',PostList.as_view(),name='post_list'),
    path('detail/<int:pk>/',PostDetail.as_view(),name='post_detail'),
]