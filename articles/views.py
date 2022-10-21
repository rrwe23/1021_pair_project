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