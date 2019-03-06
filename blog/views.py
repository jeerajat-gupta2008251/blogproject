from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.utils import timezone
from blog.forms import Postform,Commentform
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

class Aboutview(TemplateView):
	template_name='blog/about.html'

class Postlistview(ListView):
	model=Post

	def get_queryset(self):
		return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class Postdetailview(DetailView):
	model=Post

class Postcreateview(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	redirect_field_name='blog/post_list.html'
	model=Post
	form_class=Postform

class Postupdateview(LoginRequiredMixin,UpdateView):
	login_url = '/login/'
	redirect_field_name='blog/post_list.html'
	model=Post
	form_class=Postform

class Postdeleteview(LoginRequiredMixin,DeleteView):
	login_url = '/login/'
	model=Post
	success_url= reverse_lazy('post_list')

class Draftlistview(LoginRequiredMixin,ListView):
	login_url='/login/'
	redirect_field_name='blog/post_list.html'
	model=Post
	context_object_name="posts"
	template_name="blog/post_draft_list.html"
	def get_queryset(self):
		return Post.objects.filter(publish_date__isnull=True).order_by('create_date')

# @login_required
def Add_comment_to_post(request,pk):
	post1=get_object_or_404(Post,pk=pk)
	if(request.method=='POST'):
		form=Commentform(request.POST)
		if(form.is_valid()):
			comment=form.save(commit=False)
			comment.post=post1
			comment.save()
			return redirect('post_detail',pk=post1.pk)
	else:
		form=Commentform()
		return render(request,"blog/comment_form.html",{'form':form})

@login_required
def Comment_approve(request,pk):
	comment=get_object_or_404(Comment,pk=pk)
	comment.approve_comment()
	return redirect('post_detail',pk=comment.post.pk)

@login_required
def Comment_remove(request,pk):
	comment=get_object_or_404(Comment,pk=pk)
	post_pk=comment.post.pk
	comment.delete()
	return redirect('post_detail',pk=post_pk)

@login_required
def Publish_post(request,pk):
	post=get_object_or_404(Post,pk=pk)
	post.publish()
	return redirect('post_detail',pk=post.pk)









