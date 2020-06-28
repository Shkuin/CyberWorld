from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import Post, Player, Comment
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PlayerForm, CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Имя пользователя или пароль введены некорректно')

    context = {}
    return render(request, 'accounts/login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registration/register.html', context)


def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        messages.info(request, 'Username or password is incorrect')

    return render(
        request,
        'main_pages/index.html',
        {
        }
    )


def aboutUs(request):
    return render(
        request,
        'about_us/aboutUs.html',
        {
        }
    )


def articles(request):
    posts = Post.objects.all()
    return render(request, 'articles/articles.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    comments = Comment.objects.filter(post=post).order_by('-id')
    if request.method=='POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(post=post, user=request.user, text=text)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request, 'articles/post_detail/post_detail.html', context={'post': post,
                                                                             'comments': comments,
                                                                             'comment_form': comment_form})


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def courses(request):
    return render(request, 'course/course.html')


@allowed_users(allowed_roles=['players'])
@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'accounts/users/user.html', context)


@login_required(login_url='login')
def accountSettings(request):
    player = request.user.player
    form = PlayerForm(instance=player)

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/users/account_settings.html', context)
