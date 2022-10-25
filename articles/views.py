from django.shortcuts import render, redirect
from .forms import CommentForm, ReviewForm
from .models import Review, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')

    # 페이지네이션
    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    page_obj = paginator.get_page(page)

    context = {
        'reviews' : reviews,
        'question_list': page_obj,
    }
    
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=='POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('articles:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()

    context ={
        'review' : review,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request,'articles/detail.html',context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method =='POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('articles:detail', review.pk)
    else:
        review_form = ReviewForm(instance = review)

    context = {
        'review_form':review_form
    }
    return render(request, 'articles/update.html',context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('articles:index')

def create_comment(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    
    return redirect('articles:detail', review.pk)

def delete_comment(reqeust, review_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()

    return redirect('articles:detail', review_pk)

def search(request):
    search = request.GET.get('search')
    search_options = request.GET.get('Search_option')

    
    if search_options == 'movie_name__contains':
        reviews = Review.objects.filter(movie_name__contains=search)
        
    elif search_options == 'title__contains':
        reviews = Review.objects.filter(title__contains=search)

    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj,
        'search_options' : search_options,
        'search' : search
    }

    return render(request, 'articles/search.html' ,context)
@login_required
def like(request,pk):
    review = Review.objects.get(pk=pk)
    # if review.like_users.filter(id=request.user.id)exists()
    
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    
    return redirect('articles:detail',pk)
    

