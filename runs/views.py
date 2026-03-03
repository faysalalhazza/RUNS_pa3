from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, UserProfile


def login_view(request):
    """Login page — the root URL."""
    if request.user.is_authenticated:
        return redirect('stream')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('stream')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'runs/login.html')


def register_view(request):
    """Registration page."""
    if request.user.is_authenticated:
        return redirect('stream')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # Validation
        if not username or not first_name or not last_name or not password or not password2:
            messages.error(request, 'All fields are required.')
        elif password != password2:
            messages.error(request, 'Passwords do not match.')
        elif len(password) <= 6:
            messages.error(request, 'Password must be more than six characters.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('stream')

    return render(request, 'runs/register.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def stream_view(request):
    """Global stream — all posts from all users."""
    posts = Post.objects.select_related('author').all()
    return render(request, 'runs/stream.html', {'posts': posts})


@login_required
def profile_view(request, username=None):
    """Profile page for a given user (defaults to logged-in user)."""
    if username is None:
        profile_user = request.user
    else:
        profile_user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(author=profile_user)

    if request.method == 'POST' and profile_user == request.user:
        content = request.POST.get('content', '').strip()
        location = request.POST.get('location', '').strip()
        if content and len(content) <= 42:
            Post.objects.create(author=request.user, content=content, location=location)
            return redirect('profile')
        else:
            messages.error(request, 'Post must be 1–42 characters.')

    return render(request, 'runs/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
    })
