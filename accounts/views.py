from django.shortcuts import render,redirect
from .forms import SignupForm

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = SignupForm()
    context = {
        'form' : form
    }

    return render(request,'accounts/signup.html',context)

