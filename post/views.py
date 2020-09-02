from django.shortcuts import render, redirect
from post.models import Post
from post.forms import PostForm
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by("fecha_creado")[0:12]
    template = "post/index2.html"
    contexto = {"posts": posts}
    return render(request, template, contexto)


def show_post(request, id):
    post = Post.objects.get(pk=id)
    # falta filtrar que sean post del mismo usuario
    lista_mas_post = Post.objects.exclude(id=id)[0:12]
    contexto = {
        "post": post,
        "mas_post": lista_mas_post
    }
    template = "post/post2.html"
    return render(request, template, contexto)


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("post", post.id)
        else:
            template = "post/new2.html"
            contexto = {"form": form}
            return render(request, template, contexto)

    form = PostForm()

    template = "post/new2.html"
    contexto = {"form": form}

    return render(request, template, contexto)
