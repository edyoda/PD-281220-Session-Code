from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse
from datetime import date

from .forms import CommentForm
from .models import Post


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        qs = super().get_queryset()
        data = qs[:3]
        return data


class AllPostsView(ListView):
    template_name =  "blog/all_posts.html"
    model = Post
    context_object_name = "posts"


class SinglePostView(View):

    def is_read_later(self, request, post_id):
        stored_post_ids = request.session.get("stored_posts")
        if stored_post_ids is not None:
            return post_id in stored_post_ids
        return False

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm()
        print(self.is_read_later(request, post.id))
        return render(request, "blog/post_detail.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
            "comment_form": comment_form,
            "is_read_for_later": self.is_read_later(request, post.id)
        })

    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.post = post
            comment_form.save()
            url = reverse("selected-post", args=[slug,])
            return HttpResponseRedirect(url)
        return render(request, "blog/post_detail.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
            "comment_form": comment_form,
            "is_read_for_later": self.is_read_later(request, post.id)
        })


class ReadLaterView(View):

    def get(self, request):
        stored_posts_ids = request.session.get("stored_posts")
        context = {}
        if stored_posts_ids is not None:
            posts = Post.objects.filter(id__in=stored_posts_ids)
            context["posts"] = posts
            context["has_posts"] = True
        else:
            context["has_posts"] = False
        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        read_later_id = request.POST["read_later_id"]
        post_id = int(read_later_id)
        stored_posts_ids = request.session.get("stored_posts")
        if stored_posts_ids is None or len(stored_posts_ids) == 0:
            stored_posts_ids = [post_id,]
        else:
            if post_id not in stored_posts_ids:
                stored_posts_ids.append(post_id)
            else:
                stored_posts_ids.remove(post_id)
        request.session["stored_posts"] = stored_posts_ids
        return HttpResponseRedirect("/")

        