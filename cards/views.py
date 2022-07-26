from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authorizations.models import User
from cards.forms import CardForm
from cards.models import Card


@login_required(login_url='login')
def home_page(request):
    query = request.GET.get('query', None)
    if query is not None:  # text like "%...%"
        cards = Card.objects.filter(description__icontains=query).order_by('-created_at')
    else:
        cards = Card.objects.order_by('-created_at')
    context = {
        'cards': cards,
        'current_user': request.user
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def upload_card(request):
    context = {
        'current_user': request.user
    }
    if request.method == 'GET':
        context['form'] = CardForm()
        return render(request, 'add_card.html', context)
    elif request.method == 'POST':
        card = Card.objects.create(
            description=request.POST['description'],
            image=request.FILES['image'],
            user=request.user
        )
        return redirect('home')


@login_required(login_url='login')
def get_user_profile(request, user_id):
    context = {
        'user': User.objects.get(pk=user_id),
        'cards': Card.objects.filter(user_id=user_id).order_by('-created_at'),
        'current_user': request.user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def get_post_detail(request, post_id):
    context = {
        'card': Card.objects.get(pk=post_id),
        'current_user': request.user
    }
    return render(request, 'post_detail.html', context)

