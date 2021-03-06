from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from app.forms import CommentForm
from app.models import *

# Create your views here.
# Index (Home) Page
def IndexPage(request):
  template_name = 'index.html'
  category = Category.objects.all().order_by('?')[0]
  featured_posts = Blog.objects.all()[:3]
  recent_posts = Blog.objects.all().order_by('-created_at')[3:7]
  popular_post = Blog.objects.all().order_by('-created_at')[11]
  most_read_posts = Blog.objects.all().order_by('-created_at')[17:21]
  hot_post = Blog.objects.all().order_by('?')[0]
  top_of_the_week = Blog.objects.all().order_by('-created_at')[21:24]
  counts = []

  for c in Category.objects.all():
    counts.append(Blog.objects.filter(category=c).count())

  category_counts = zip(Category.objects.all(), counts)

  context = {
    'featured_posts': featured_posts,
    'recent_posts': recent_posts,
    'popular_post': popular_post,
    'most_read_posts': most_read_posts,
    'hot_post': hot_post,
    'top_of_the_week': top_of_the_week,
    'category': category,
    'category_counts': category_counts,
  }

  return render(request, template_name, context)

# Blog Page
def BlogHome(request, slug):
  template_name = 'blog.html'
  category = get_object_or_404(Category, slug=slug)
  page = request.GET.get('page', 1)
  search = request.GET.get('search')

  if search:
    post_list = Blog.objects.filter(Q(title__icontains=search) | Q(content__icontains=search) | Q(category__name__icontains=search) | (Q(author__icontains=search)))
  else:
    post_list = Blog.objects.filter(category__slug=slug)

  paginator = Paginator(post_list, 3)
  
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)

  context = {
    'posts': posts,
    'category': category,
  }

  return render(request, template_name, context)

# Blog Details Page
def PostDetails(request, slug):
  template_name = "article.html"
  form = CommentForm()
  search = request.GET.get('search')
  post = None
  post_comments = None
  search_posts = None

  if search:
    search_post_list = Blog.objects.filter(Q(title__icontains=search) | Q(content__icontains=search) | Q(category__name__icontains=search) | (Q(author__icontains=search)))
    
    page = request.GET.get('page', 1)
    paginator = Paginator(search_post_list, 3)
    
    try:
      sp = paginator.page(page)
      search_posts = sp
    except PageNotAnInteger:
      sp = paginator.page(1)
      search_posts = sp
    except EmptyPage:
      sp = paginator.page(paginator.num_pages)
      search_posts = sp
  else:
    post = get_object_or_404(Blog, slug=slug)
    
    if request.method == "POST":
      form = CommentForm(request.POST or None)
      if form.is_valid():
        c = form.save(commit=False)
        c.post = post
        c.save()

        return redirect('post_details', slug=slug)

    pc = Comment.objects.filter(post=post)
    post_comments = pc


  context = {
    'post': post,
    'search_posts': search_posts,
    'form': form,
    'post_comments': post_comments,
  }

  return render(request, template_name, context)

# 404 Page
def page_404(request, exception):
  template_name = 'page404.html'

  return render(request, template_name)