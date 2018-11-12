from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm,UserLoginForm
from django.urls import reverse
from .models import LoginUser


def user_register(request):
    context = dict()
    form = UserRegisterForm()
    print(request.FILES)
    if request.method == 'POST':
        url_name = 'register_fail'
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            result = form.save()
            if result:
                url_name = 'register_success'
            else:
                context['form'] = form
                return render(request, 'modelform/register_fail.html', context)
        return HttpResponseRedirect(reverse('modelform:' + url_name))
    context['form'] = form
    return render(request, 'modelform/register.html', context)

def register_fail(request):
    context = dict()
    return render(request,'modelform/register_fail.html',context)

def register_success(request):
    context = dict()
    return render(request,'modelform/register_success.html',context)


def user_login(request):
    context = dict()
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = LoginUser.objects.filter(username=username,password=password)
            if user:
                user = user[0]
                login_user = dict(username=user.username,portrait=str(user.portrait),
                                  nickname=user.nickname)
                request.session['login_user'] = login_user
                return HttpResponseRedirect(reverse('modelform:user_index'))
            else:
                context['error_message'] = '账号或密码错误'
    context['form'] = form
    return render(request,'modelform/user_login.html',context)

def user_index(request):
    context = dict()
    login_user = request.session.get('login_user',None)
    if not login_user:
        return HttpResponseRedirect(reverse('modelform:user_login'))
    context['user'] = login_user
    context['login_user'] = LoginUser.objects.get(username=login_user['username'])
    return render(request,'modelform/user_index.html',context)

def user_logout(request):
    login_user = request.session.get('login_user', None)
    if login_user:
        request.session.pop('login_user')
        print(dir(request.session))
    return HttpResponseRedirect(reverse('modelform:user_login'))

