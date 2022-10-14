from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'reviews/create.html', context)


def index(request):
    users = Review.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'reviews/index.html', context)