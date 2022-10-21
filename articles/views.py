from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews' : reviews
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=='POST':
        form = ReviewForm(request.POST)
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
    

    context ={
        'review' : review,

    }
    return render(request,'articles/detail.html',context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method =='POST':
        review_form = ReviewForm(request.POST,instance= review)
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