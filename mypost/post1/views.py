from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q

# Create your views here.
def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post1/homepage.html', {'posts':posts})

def post_new(request): 
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail",pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'post1/post_add.html',{'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post1/post_detail.html',{'post':post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'post1/post_add.html',{'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')

def post_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(name__icontains=query)|Q(text__icontains=query)
            results = Post.objects.filter(lookups).distinct()
            context = {'results':results, 'submitbutton':submitbutton}
            return render(request, 'post1/post_search.html', context)
        else:
            return render(request, 'post1/post_search.html')
    else:
        return render(request, 'post1/post_search.html')
