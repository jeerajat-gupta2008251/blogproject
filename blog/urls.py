from django.conf.urls import url 
from . import views

urlpatterns=[
     url(r'^about/$',views.Aboutview.as_view(),name="about"),
     url(r'^$',views.Postlistview.as_view(),name="post_list"),
     url(r'^post/(?P<pk>\d+)$',views.Postdetailview.as_view(),name="post_detail"),
     url(r'^post/new/$',views.Postcreateview.as_view(),name="post_new"),
     url(r'^post/(?P<pk>\d+)/update/$',views.Postupdateview.as_view(),name="post_update"),
     url(r'^post/(?P<pk>\d+)/delete/$',views.Postdeleteview.as_view(),name="post_delete"),
     url(r'^draft/$',views.Draftlistview.as_view(),name="draft"),
     url(r'^post/(?P<pk>\d+)/addcomment/$',views.Add_comment_to_post,name="add_comment_to_post"),
     url(r'^post/(?P<pk>\d+)/approve/$',views.Comment_approve,name="comment_approve"),
     url(r'^post/(?P<pk>\d+)/removecomment/$',views.Comment_remove,name="comment_remove"),
     url(r'^post/(?P<pk>\d+)/publish/$',views.Publish_post,name="publish_post"),

]